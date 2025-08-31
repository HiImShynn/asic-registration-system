from datetime import date, datetime
from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from enum import Enum
from .enums.asic_enums import StateTerritoryCodeType, COUNTRY, STREET_TYPES, AddressTypeType

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

class UnstructuredAddressType(ASICBaseModel):
    addressLine1: Annotated[str, Field(description="The first line of the address")]
    addressLine2: Annotated[str, Field(description="The second line of the address")]
    addressLine3: Optional[Annotated[str, Field(description="The third line of the address")]] = None
    addressLine4: Optional[Annotated[str, Field(description="The fourth line of the address")]] = None

class SemiStructuredPhysicalAddressType(ASICBaseModel):
    addressLine1: Annotated[str, Field(description="The first line of the address")]
    addressLine2: Optional[Annotated[str, Field(description="The third line of the address")]] = None
    locality: Annotated[str, Field(description="The locality of the address")]
    state: Annotated[StateTerritoryCodeType, Field(description="The state or territory of the address")]
    postCode: Annotated[str, Field(description="The postal code of the address", pattern=r"^\d{4}$")]

class AddressLodgeType(ASICBaseModel):

    type: Annotated[AddressTypeType, Field(description="The type of address")]
    careOf: Optional[Annotated[str, Field(description="Care of name for the address")]] = None
    country: Optional[Annotated[str, Field(description="The country of the address", default="Australia")]] = None
    startDate: Optional[Annotated[date, Field(description="The start date of the address")]] = None
    postalDeliveryType: Optional[Annotated[str, Field(description="The postal delivery type of the address")]] = None

    @model_validator(mode="after")
    def check_postal_delivery_type(self):
        tval = self.type.value if hasattr(self.type, 'value') else self.type
        if self.postalDeliveryType is not None and tval != "GE":
            raise ValueError("postalDeliveryType can only be set for addresses of type 'GE'.")
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
