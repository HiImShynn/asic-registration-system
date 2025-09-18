from pydantic import Field, model_validator, field_validator
from typing import Optional, Annotated
from apps.common.models import ASICBaseModel

class Proprietor(ASICBaseModel):
    """Proprietor model for query name availability"""
    proprietorAcn: Optional[Annotated[str, Field(pattern=r"^\d{9}$", description="The ACN of the proprietor")]] = None
    proprietorAbn: Optional[Annotated[str, Field(pattern=r"^\d{11}$", description="The ABN of the proprietor")]] = None

    @model_validator(mode="after")
    def validate_exactly_one_identifier(self):
        """Ensure exactly one of ACN or ABN is provided"""
        has_acn = self.proprietorAcn is not None
        has_abn = self.proprietorAbn is not None
        
        if not (has_acn ^ has_abn):  # XOR - exactly one must be true
            raise ValueError("Exactly one of proprietorAcn or proprietorAbn must be provided")
        
        return self

class QueryNameAvailabilityBody(ASICBaseModel):
    """Request body for query name availability"""
    proposedName: Annotated[
        str, 
        Field(
            min_length=1,
            max_length=200,
            description="The proposed name to check availability for (must be UPPERCASE)"
        )
    ]
    companyNameAvailabilityCheck: Optional[Annotated[bool, Field(description="Whether to check company name availability")]] = None
    bnNameAvailabilityCheck: Optional[Annotated[bool, Field(description="Whether to check business name availability")]] = None
    proprietor: Optional[Annotated[Proprietor, Field(description="The proprietor details for same holder exemption")]] = None

    @field_validator("proposedName")
    def validate_proposed_name(cls, value: str) -> str:
        """Validate proposed name format and characters according to ASIC rules"""
        if not value:
            raise ValueError("proposedName must not be empty")
        
        # Must be uppercase
        if value != value.upper():
            raise ValueError("proposedName must be in UPPERCASE")
        
        # ASIC allowed characters: A-Z, 0-9, spaces, and specific punctuation/symbols
        # Based on ASIC documentation: . , ? ! ( ) { } : ; ' " " | - ) _ \ / @ # $ % * = &
        valid_chars = set(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '  # Letters, numbers, space
            '.,?!(){}:;\'""|-)_\\/'  # Standard punctuation (note: ") appears twice in ASIC spec
            '@#$%*=&'  # Business symbols
        )

        invalid_chars = set(value) - valid_chars
        if invalid_chars:
            invalid_list = ', '.join(f"'{char}'" for char in sorted(invalid_chars))
            raise ValueError(
                f"proposedName contains invalid characters: {invalid_list}. "
                f"Allowed characters: A-Z, 0-9, spaces, and punctuation: . , ? ! ( ) {{ }} : ; ' \" \" | - ) _ \\ / @ # $ % * = &"
            )
        return value
    
    @model_validator(mode="after")
    def validate_availability_check(self):
        """Ensure exactly one availability check is specified"""
        company_check = self.companyNameAvailabilityCheck is True
        bn_check = self.bnNameAvailabilityCheck is True

        if not (company_check ^ bn_check):  # XOR - exactly one must be true
            raise ValueError("Exactly one of companyNameAvailabilityCheck or bnNameAvailabilityCheck must be true")
        
        return self
    
    @model_validator(mode="after")
    def validate_proprietor_usage(self):
        """Validate proprietor field usage rules"""
        if self.proprietor is not None:
            if not self.bnNameAvailabilityCheck:
                raise ValueError("proprietor can only be provided when bnNameAvailabilityCheck is true")
        
        return self
