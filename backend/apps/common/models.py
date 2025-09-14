from datetime import date, datetime
from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator, EmailStr
from enum import Enum
from .enums.asic_enums import StateTerritoryCodeType, COUNTRY, STREET_TYPES, AddressTypeType, EntityType

class ASICBaseModel(BaseModel):
    """Base model with common config for all ASIC models"""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True,
        exclude_none=True,
    ) # type: ignore

## Person & Identity Models
### 2. PersonName Hierarchy (All Individual-related Endpoints)
class PersonNameType(ASICBaseModel):
    givenNames: Annotated[str, Field(description="The person's given names")]
    otherGivenNames: Optional[Annotated[str, Field(description="The person's other given names")]] = None
    familyName: Annotated[str, Field(description="The person's family name")]

class PersonNameLodgeType(PersonNameType):
    pass

class PersonNameOptionalType(ASICBaseModel):
    """PersonNameOptionalType for searchNni variants"""
    givenNames: Annotated[Optional[str], Field(description="The person's given names")]
    otherGivenNames: Optional[Annotated[str, Field(description="The person's other given names")]] = None
    familyName: Annotated[Optional[str], Field(description="The person's family name")]

class PersonNameWithRoleType(PersonNameType):
    role: Annotated[str, Field(description="The person's role")]

### 3. BirthDetails Hierarchy
class BirthDetailsType(BaseModel):
    """BirthDetailsType for retrieval"""
    date: Annotated[date, Field(description="The person's date of birth")]
    cityTown: Optional[Annotated[str, Field(description="The person's city or town of birth")]] = None
    state: Optional[Annotated[StateTerritoryCodeType, Field(description="The person's state or territory of birth")]] = None
    countryOfBirth: Annotated[str, Field(description="The person's country of birth")]

    @field_validator('countryOfBirth')
    def validate_country(cls, v):
        v_stripped = v.strip() if isinstance(v, str) else v
        if v_stripped not in COUNTRY:
            raise ValueError(f"countryOfBirth must be one of the defined countries.")
        return v_stripped
    
    @field_validator('cityTown')
    def validate_city_town(cls, v):
        if v is not None:
            return v.title()
        return v
    
    @field_validator('date')
    def validate_birth_date(cls, v):
        from datetime import date as date_type
        if v >= date_type.today():
            raise ValueError("Birth date must be before current date.")
        return v

class BirthDetailsLodgeType(BirthDetailsType):
    pass

class BirthDetailsExtType(BirthDetailsType):
    """BirthDetailsExtType for external use"""
    pass

## Address Models Hierarchy
### Address Type System for all Endpoints

class PhysicalAddressType(ASICBaseModel):
    """PhysicalAddressType for all Australian physical address-related endpoints"""
    floorNumber: Optional[Annotated[str, Field(description="The floor number of the address")]] = None
    propertyName: Optional[Annotated[str, Field(description="The property name of the address")]] = None
    unitOrOfficeNumber: Optional[Annotated[str, Field(description="The unit or office number of the address")]] = None
    streetNumber: Optional[Annotated[str, Field(description="The street number of the address")]] = None
    streetName: Optional[Annotated[str, Field(description="The street name of the address")]] = None
    streetType: Optional[Annotated[str, Field(description="The street type of the address")]] = None
    postalDeliveryType: Optional[Annotated[str, Field(description="The postal delivery type of the address")]] = None
    postalDeliveryNumber: Optional[Annotated[str, Field(description="The postal delivery number of the address")]] = None
    locality: Annotated[str, Field(description="The locality of the address")]
    state: Annotated[StateTerritoryCodeType, Field(description="The state or territory of the address")]
    postCode: Annotated[str, Field(description="The postal code of the address", pattern=r"^\d{4}$")]

    @field_validator('streetType')
    def validate_street_type(cls, v):
        if v is not None:
            v_stripped = v.strip()
            if v_stripped not in STREET_TYPES:
                raise ValueError(f"streetType must be one of the defined street types.")
            return v_stripped
        return v

    @field_validator('locality')
    def validate_locality(cls, v):
        if v is not None:
            return v.title()
        return v
    
class UnstructuredAddressType(ASICBaseModel):
    addressLine1: Annotated[str, Field(description="The first line of the address")]
    addressLine2: Annotated[str, Field(description="The second line of the address")]
    addressLine3: Optional[Annotated[str, Field(description="The third line of the address")]] = None
    addressLine4: Optional[Annotated[str, Field(description="The fourth line of the address")]] = None

class SemiStructuredPhysicalAddressType(ASICBaseModel):
    addressLine1: Annotated[str, Field(description="The first line of the address")]
    addressLine2: Optional[Annotated[str, Field(description="The second line of the address")]] = None
    locality: Annotated[str, Field(description="The locality of the address")]
    state: Annotated[StateTerritoryCodeType, Field(description="The state or territory of the address")]
    postCode: Annotated[str, Field(description="The postal code of the address", pattern=r"^\d{4}$")]

class AddressLodgeBaseType(ASICBaseModel):
    """Base model for address lodge types."""
    type: Annotated[AddressTypeType, Field(description="The type of address")]
    careOf: Optional[Annotated[str, Field(description="Care of name for the address")]] = None
    country: Optional[Annotated[str, Field(description="The country of the address", default="Australia")]] = None
    startDate: Optional[Annotated[date, Field(description="The start date of the address")]] = None

class AddressLodgeType(AddressLodgeBaseType, PhysicalAddressType):
    """
    Model for address lodge types. 
    This does not allow unstructured addresses.
    Only physical addresses of Australia and of type "GE" or "GD" are allowed.
    """
    @model_validator(mode="after")
    def check_postal_delivery_type(self):
        tval = self.type.value if hasattr(self.type, 'value') else self.type
        if self.postalDeliveryType is not None and tval != "GE":
            raise ValueError("postalDeliveryType can only be set for addresses of type 'GE' (address for service).")
        return self

    @field_validator('type')
    def validate_type(cls, v):
        if v not in ("GD", "GE"):
            raise ValueError("type must be either 'GD' (principal place of business) or 'GE' (service of documents address)")
        return v

    @field_validator('country')
    def validate_country(cls, v):
        if v is not None:
            v_stripped = v.strip().lower()
            if v_stripped != "australia":
                raise ValueError("country must be 'Australia' for this address type")
            return "Australia"
        return v

# Example parent model enforcing both GD and GE, both Australian
class AddressLodgeListModel(BaseModel):
    addresses: List[AddressLodgeType]

    @model_validator(mode="after")
    def check_gd_ge(self):
        type_values = [a.type.value if hasattr(a.type, 'value') else a.type for a in self.addresses]
        if type_values.count("GD") != 1 or type_values.count("GE") != 1:
            raise ValueError("Exactly one GD and one GE address are required.")
        for a in self.addresses:
            tval = a.type.value if hasattr(a.type, 'value') else a.type
            if (tval in ("GD", "GE")) and (a.country is None or a.country.strip().lower() != "australia"):
                raise ValueError(f"Address of type {tval} must have country 'Australia'.")
        return self

## AbrEntity Types

class Abn(ASICBaseModel):
    """
    Model for Australian Business Number (ABN).
    """
    abn: Annotated[str, Field(description="The Australian Business Number (ABN)", pattern=r"^\d{11}$")]

class AbnReferenceNumber(ASICBaseModel):
    """
    Model for Australian Business Number (ABN) reference numbers.
    """
    referenceNumber: Annotated[str, Field(description="The reference number for the ABN", pattern=r"^\d{1,10}$")]

class AbrEntity(ASICBaseModel):
    """
    Model for Australian Business Register (ABR) entities.
    """
    abn: Optional[Annotated[Abn, Field(description="The Australian Business Number (ABN)")]] = None
    referenceNumber: Optional[Annotated[AbnReferenceNumber, Field(description="The reference number for the ABN")]] = None
    entityName: Optional[Annotated[str, Field(description="The name of the entity")]] = None
    entityType: Optional[Annotated[EntityType, Field(description="The type of the entity")]] = None
    abnExemption: Optional[Annotated[bool, Field(description="Indicates if the entity is exempt from having an ABN as a Joint Venture")]] = False

## Individual Types

class IndividualPhysicalAddressLodgeType(AddressLodgeBaseType, PhysicalAddressType):
    """
    Model for individual physical address lodge types.
    Must be type GC (residential address) and Australian address.
    Postal delivery types are not allowed for individual addresses.
    """
    @field_validator('type')
    def validate_type(cls, v):
        # RESIDENTIAL_ADDRESS_BUSINESS_NAMES
        if v != "GC":
            raise ValueError("type must be 'GC' (Residential address business names)")
        return v
    
    @field_validator('country')
    def validate_country(cls, v):
        if v is not None:
            v_stripped = v.strip().lower()
            if v_stripped != "australia":
                raise ValueError("country must be 'Australia' for individual addresses")
            return "Australia"
        return "Australia"  # Default to Australia if None
    
    @model_validator(mode="after")
    def validate_no_postal_delivery(self):
        if self.postalDeliveryType is not None:
            raise ValueError("postalDeliveryType is not allowed for individual residential addresses (type GC)")
        return self

class IndividualUnstructuredAddressLodgeType(AddressLodgeBaseType, UnstructuredAddressType):
    """
    Model for individual unstructured address lodge types (for foreign addresses).
    Must be type GC (residential address) and must NOT be Australian address.
    """
    @field_validator('type')
    def validate_type(cls, v):
        if v != "GC":
            raise ValueError("type must be 'GC' (Residential address business names)")
        return v
    
    @field_validator('country')
    def validate_country(cls, v):
        if v is not None:
            v_stripped = v.strip().lower()
            if v_stripped == "australia":
                raise ValueError("Use IndividualPhysicalAddressLodgeType for Australian addresses")
            if v_stripped not in [c.lower() for c in COUNTRY]:
                raise ValueError("country must be one of the defined countries")
            return v.title()  # Return in title case
        # Country is required for unstructured addresses (foreign addresses)
        raise ValueError("country is required for unstructured addresses")

### Choose "Individual" for sole traders
class IndividualLodgeType(ASICBaseModel):
    """
    Complete individual lodge model for business name registration.
    
    Business Rules:
    - Individual section is conditional (mandatory only when holder type is individual)
    - Address must be type "GC" (residential address)
    - Australian addresses use structured format, foreign addresses use unstructured
    - Email is optional and private data
    """
    name: Annotated[PersonNameLodgeType, Field(description="The individual's name")]
    birthDetails: Annotated[BirthDetailsLodgeType, Field(description="The individual's birth details")]
    address: Annotated[
        IndividualPhysicalAddressLodgeType | IndividualUnstructuredAddressLodgeType, 
        Field(union_mode='smart', description="Individual's residential address")
    ]
    emailAddress: Optional[EmailStr] = Field(None, description="Optional email address (private data)")
    
    @model_validator(mode="after")
    def validate_address_country_consistency(self):
        """Ensure address type matches country requirements"""
        if isinstance(self.address, IndividualPhysicalAddressLodgeType):
            # Australian addresses must use structured format
            if not self.address.country or self.address.country.lower() != "australia":
                raise ValueError("IndividualPhysicalAddressLodgeType is only for Australian addresses")
        elif isinstance(self.address, IndividualUnstructuredAddressLodgeType):
            # Foreign addresses must use unstructured format
            if not self.address.country or self.address.country.lower() == "australia":
                raise ValueError("IndividualUnstructuredAddressLodgeType is only for foreign addresses")
        return self

## Organisation Types
### Choose "Organisation" for companies, partnerships, trusts

class OrganisationLodgeType(ASICBaseModel):
    """
    Model for organisation lodge types.
    """
    name: Annotated[str, Field(description="The organisation's name")]
    acn: Optional[Annotated[str, Field(description="The Australian Company Number (ACN)", pattern=r"^\d{9}$")]] = None
    emailAddress: Optional[EmailStr] = Field(None, description="Optional email address (private data)")

## Associate Types

### These types only required for: 
#### Partnership (PTSH) -> must include partner details
#### Joint Venture (JV) -> must include JV partner details
#### Unincorporated Structure (USTR) -> must include trustee details
class AssociateLodgeBaseType(ASICBaseModel):
    """
    Model for associate lodge types.
    Maximum 500 associates allowed.
    """
    abrEntity: Optional[Annotated[AbrEntity, Field(description="The ABR entity details of the associate")]] = None
    abn: Annotated[Abn, Field(description="The Australian Business Number (ABN) of the associate")]
    # 1. Conditional as follows:
    # 1) Mandatory if the holder is an unincorporated structure, a partnership or a joint venture.
    # IF the entity type = PTSH (partnership) or JV (Joint venture): It must contain the partner’s details of the partnership or in a joint venture
    # IF the entity type = USTR (unincorporated entities): It must contain the organisation representatives details for the entity (for example the trustees)
    # 2) Not required if holder ‘Individual’ or ‘incorporated body’ (e.g. companies)

class AssociateLodgeIndividualType(AssociateLodgeBaseType):
    """
    Model for individual associate lodge types.
    """
    individual: Annotated[IndividualLodgeType, Field(description="The individual's details")]

class AssociateLodgeOrganisationType(AssociateLodgeBaseType):
    """
    Model for organisation associate lodge types.
    """
    organisation: Annotated[OrganisationLodgeType, Field(description="The organisation's details")]

class PartnerAssociateLodgeType(BaseModel):
    """
    Model for partner associate lodge types.
    Maximum 9 partner associates allowed.
    """
    associate: Annotated[
        IndividualLodgeType | OrganisationLodgeType,
        Field(union_mode='smart', description="The associate details, which can be an individual or organisation")
    ]

class SignatoryLodgeType(BaseModel):
    """
    Model for signatory lodge types.
    """
    name: Annotated[PersonNameType, Field(description="The signatory's name")]
    dateSigned: Annotated[date, Field(description="The date the document was signed", default_factory=lambda: datetime.now().date())]
    declaresTrueAndCorrect: Annotated[bool, Field(description="Declaration of truth and correctness")]
