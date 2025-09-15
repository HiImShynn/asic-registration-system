from datetime import date
from typing import Annotated, Optional, List, Union
from pydantic import Field, computed_field, model_validator
from apps.common.models import (
    ASICBaseModel, AbrEntity, IndividualLodgeType, OrganisationLodgeType,
    AssociateLodgeBaseType, AssociateLodgeIndividualType, AssociateLodgeOrganisationType
)
from apps.common.enums.asic_enums import OwnerType

class PartnerAssociateLodgeType(ASICBaseModel):
    """
    Represents organization representatives for unincorporated partners in PTSH/JV.
    
    From ASIC docs: When a partner cannot provide ACN/ARBN, they become "unincorporated"
    and must provide organization representatives (trustees, executives, etc.)
    """
    # Either individual representative or organisation representation
    individual: Optional[IndividualLodgeType] = None
    organisation: Optional[OrganisationLodgeType] = None

    @model_validator(mode='after')
    def validate_representative_exclusive(self):
        """Must have exactly one type of representative"""
        has_individual = self.individual is not None
        has_organisation = self.organisation is not None

        if not has_individual and not has_organisation:
            raise ValueError("PARTNER_ASSOC_REQUIRED: Must have either individual or organisation representative")
        
        if has_individual and has_organisation:
            raise ValueError("PARTNER_ASSOC_EXCLUSIVE: Cannot have both individual and organisation representative")
        
        # Organisation representatives must have ACN (they represent the unincorporated entity)
        if self.organisation and not self.organisation.acn:
            raise ValueError("PARTNER_ASSOC_ORG_ACN: Organisation representatives must have ACN")
        
        return self

class AssociateLodgeType(ASICBaseModel):
    """
    Enhanced associate model that handles dynamic partner classification.
    
    This replaces existing AssociateLodgeIndividualType/AssociateLodgeOrganisationType
    with a unified model that can handle the unincorporated partner scenario.
    """
    
    # Core associate info (ABR entity required for all associates)
    abrEntity: Annotated[AbrEntity, Field(description="The ABR entity details of the associate")]

    # Associate details (Individual or Organisation, not both)
    individual: Optional[Annotated[IndividualLodgeType, Field(description="The individual's details")]] = None
    organisation: Optional[Annotated[OrganisationLodgeType, Field(description="The organisation's details")]] = None
    
    # Organization representatives (only for unincorporated organisation partners)
    partnerAssociate: Optional[Annotated[List[PartnerAssociateLodgeType], Field(description="The partner associate details")]] = None

    # Metadata fields
    startDate: Optional[Annotated[date, Field(description="The start date of the association")]] = None
    endDate: Optional[Annotated[date, Field(description="The end date of the association")]] = None

    @computed_field
    @property
    def partner_classification(self) -> str:
        """
        Dynamically classify this associate:
        - "individual": Individual person
        - "incorporated": Organisation with ACN/ARBN
        - "unincorporated": Organisation without ACN/ARBN (needs representatives)
        """
        if self.individual and not self.organisation:
            return "individual"
        elif self.organisation and not self.individual:
            if self.organisation.acn:
                return "incorporated" 
            else:
                return "unincorporated"
        else:
            raise ValueError("ASSOC_STRUCTURE: Associate must be either individual or organisation")

    @computed_field
    @property
    def requires_representatives(self) -> bool:
        """Check if this associate needs organisation representatives"""
        return self.partner_classification == "unincorporated"

    @model_validator(mode='after')
    def validate_associate_classification_rules(self):
        """Apply validation rules based on partner classification"""
        
        classification = self.partner_classification
        
        if classification == "individual":
            # Individual associate rules
            if self.partnerAssociate:
                raise ValueError("IND_ASSOC_NO_REPS: Individual associates cannot have organization representatives")
            
            if not self.abrEntity.abn:
                raise ValueError("IND_ASSOC_ABN: Individual associates must have ABN")
        
        elif classification == "incorporated":
            # Incorporated associate rules
            if self.partnerAssociate:
                raise ValueError("INC_ASSOC_NO_REPS: Incorporated associates cannot have organization representatives")
            
            if self.organisation and self.organisation.acn:
                raise ValueError("INC_ASSOC_ACN: Incorporated associates must have ACN")
            
            if not self.abrEntity.abn:
                raise ValueError("INC_ASSOC_ABN: Incorporated associates must have ABN")
        
        elif classification == "unincorporated":
            # Unincorporated associate rules (inherits USTR-like requirements)
            if not self.partnerAssociate or len(self.partnerAssociate) == 0:
                raise ValueError("UNINC_ASSOC_REPS_REQUIRED: Unincorporated associates must have organization representatives")
            
            if self.organisation and self.organisation.acn:
                raise ValueError("UNINC_ASSOC_NO_ACN: Unincorporated associates cannot have ACN")
            
            if not self.abrEntity.abn:
                raise ValueError("UNINC_ASSOC_ABN: Unincorporated associates must have ABN")
            
            # Validate each representative
            for i, rep in enumerate(self.partnerAssociate):
                try:
                    rep.model_validate(rep.model_dump())
                except Exception as e:
                    raise ValueError(f"UNINC_REP_INVALID: Representative {i+1} validation failed: {str(e)}")
        
        return self
    
    def get_primary_name(self) -> str:
        """Get the primary name for this associate"""
        if self.individual:
            return f"{self.individual.name.givenNames} {self.individual.name.familyName}".strip()
        elif self.organisation:
            return self.organisation.name
        return "Unknown Associate"
    
    def get_representative_summary(self) -> dict:
        """Get summary of representatives for unincorporated associates"""
        if not self.requires_representatives:
            return {"has_representatives": False}
        
        summary = {
            "has_representatives": True,
            "representative_count": len(self.partnerAssociate) if self.partnerAssociate else 0,
            "representatives": []
        }
        
        if self.partnerAssociate:
            for rep in self.partnerAssociate:
                if rep.individual:
                    summary["representatives"].append({
                        "type": "individual",
                        "name": f"{rep.individual.name.givenNames} {rep.individual.name.familyName}".strip()
                    })
                elif rep.organisation:
                    summary["representatives"].append({
                        "type": "organisation",
                        "name": rep.organisation.name,
                        "acn": rep.organisation.acn
                    })
        
        return summary
class BusinessEntityLodgeType(ASICBaseModel):
    """
    Main business entity model that handles all owner types using conditional validation.
    This integrates with existing sophisticated models.
    """
    ownerType: Annotated[OwnerType, Field(description="The type of owner")]
    abrEntity: Optional[Annotated[AbrEntity, Field(description="ABR entity information")]] = None
    abnExemption: Optional[Annotated[bool, Field(description="ABN exemption status")]] = False

    # Conditional fields based on ownerType
    individual: Optional[IndividualLodgeType] = None
    organisation: Optional[OrganisationLodgeType] = None
    
    # Associate with dynamic classification
    associate: Optional[Annotated[List[AssociateLodgeType], Field(description="List of associates/partners")]] = None

    # Review date
    dateReview: Optional[Annotated[date, Field(description="Date of review")]] = None

    @model_validator(mode='after')
    def validate_owner_type_conditional_rules(self):
        """Your existing validation logic - enhanced to work with new associate model"""
        
        # RULE SET 1: IND (Individual) Validation
        if self.ownerType == OwnerType.IND:
            if not self.abrEntity:
                raise ValueError("IND_ABR_REQUIRED: ABR entity information is required for individuals")
            if not self.individual:
                raise ValueError("IND_INDIVIDUAL_REQUIRED: Individual details are required for sole traders")
            if self.associate and len(self.associate) > 0:
                raise ValueError("IND_NO_ASSOCIATES: Individual businesses cannot have partners or associates")
            if self.organisation:
                raise ValueError("IND_NO_ORGANISATION: Individual businesses don't need organisation details")
        
        # RULE SET 2: IB (Incorporated Body) Validation  
        elif self.ownerType == OwnerType.IB:
            if not self.abrEntity:
                raise ValueError("IB_ABR_REQUIRED: ABR entity information is required for companies")
            if not self.organisation:
                raise ValueError("IB_ORGANISATION_REQUIRED: Organisation details are required for companies")
            if self.associate and len(self.associate) > 0:
                raise ValueError("IB_NO_ASSOCIATES: Companies cannot have partners or associates")
            if self.individual:
                raise ValueError("IB_NO_INDIVIDUAL: Company applications don't need individual details")
            if self.organisation and not self.organisation.acn:
                raise ValueError("IB_ACN_REQUIRED: ACN is required for incorporated bodies")
        
        # RULE SET 3: PTSH (Partnership) Validation - Enhanced
        elif self.ownerType == OwnerType.PTSH:
            if not self.abrEntity:
                raise ValueError("PTSH_ABR_REQUIRED: ABR entity information is required for partnerships")
            if not self.organisation:
                raise ValueError("PTSH_ORGANISATION_REQUIRED: Partnership organisation details are required")
            if not self.associate or len(self.associate) == 0:
                raise ValueError("PTSH_PARTNERS_REQUIRED: Partnerships must have at least one partner")
            if len(self.associate) > 9:
                raise ValueError("PTSH_MAX_PARTNERS: Partnerships can have maximum 9 partners")
            if self.individual:
                raise ValueError("PTSH_NO_INDIVIDUAL: Partnership applications use organisation details, not individual")
            
            # Partnership cannot have ACN at top level
            if self.organisation.acn:
                raise ValueError("PTSH_NO_ACN: Partnership organisation cannot have ACN")
            
            # Validate each partner (now with dynamic classification)
            self._validate_partners_with_dynamic_classification("PTSH")
        
        # RULE SET 4: USTR (Unincorporated Entity) Validation
        elif self.ownerType == OwnerType.USTR:
            if not self.abrEntity:
                raise ValueError("USTR_ABR_REQUIRED: ABR entity information is required for trusts/associations")
            if not self.organisation:
                raise ValueError("USTR_ORGANISATION_REQUIRED: Organisation details are required for trusts/associations")
            if not self.associate or len(self.associate) == 0:
                raise ValueError("USTR_TRUSTEES_REQUIRED: Trusts/associations must have at least one trustee or representative")
            if self.individual:
                raise ValueError("USTR_NO_INDIVIDUAL: Trust/association applications use organisation details")
        
        # RULE SET 5: JV (Joint Venture) Validation - Enhanced
        elif self.ownerType == OwnerType.JV:
            if not self.organisation:
                raise ValueError("JV_ORGANISATION_REQUIRED: Organisation details are required for joint ventures")
            if not self.associate or len(self.associate) == 0:
                raise ValueError("JV_PARTNERS_REQUIRED: Joint ventures must have at least one partner")
            if len(self.associate) < 2:
                raise ValueError("JV_MIN_PARTNERS: Joint ventures must have at least 2 partners")
            
            # Special JV ABN logic
            has_abn = self.abrEntity and self.abrEntity.abn
            is_exempt = self.abnExemption is True
            if not has_abn and not is_exempt:
                raise ValueError("JV_ABN_OR_EXEMPT: Joint venture must have ABN or be ABN exempt")
            if has_abn and is_exempt:
                raise ValueError("JV_ABN_AND_EXEMPT_CONFLICT: Cannot have both ABN and abnExemption=true")
            
            # JV cannot have ACN at top level
            if self.organisation.acn:
                raise ValueError("JV_NO_ACN: Joint venture organisation cannot have ACN")
            
            if self.individual:
                raise ValueError("JV_NO_INDIVIDUAL: Joint venture applications use organisation details")
            
            # When JV is ABN exempt, all partners MUST have ABN
            if is_exempt:
                for i, partner in enumerate(self.associate):
                    if not partner.abrEntity or not partner.abrEntity.abn:
                        raise ValueError(f"JV_EXEMPT_PARTNER_ABN: When JV is ABN exempt, partner {i+1} must have ABN")
            
            # Validate each partner (now with dynamic classification and owner-type-specific rules)
            self._validate_partners_with_dynamic_classification("JV")
        
        # Validate consistency across all associates
        self._validate_associate_consistency()
        
        return self
    
    def _validate_associate_consistency(self):
            """
            Placeholder for associate consistency checks.
            Implement cross-associate validation logic here if needed.
            Currently does nothing.
            """
            pass
    
    def _validate_partners_with_dynamic_classification(self, context: str):
        """
        Helper method to validate partners with dynamic classification.
        This handles the unincorporated partner representatives logic.
        """
        if not self.associate:
            return
        for i, partner in enumerate(self.associate):
            try:
                # Trigger partner's own validation (which includes classification rules)
                partner.model_validate(partner.model_dump())
                
                # Additional context-specific validation
                if context == "PTSH":
                    # Partnership-specific partner rules
                    pass
                elif context == "JV":
                    # JV-specific partner rules  
                    pass
                    
            except Exception as e:
                raise ValueError(f"{context}_PARTNER_INVALID: Partner {i+1} validation failed: {str(e)}")
    
    @model_validator(mode="after")
    def validate_cross_field_relationships(self):
        """Your existing cross-field validation - enhanced"""
        
        # ABN and entity name consistency
        if self.abrEntity and self.organisation:
            abr_name = self.abrEntity.entityName
            org_name = self.organisation.name
            
            if abr_name and org_name and abr_name.strip() != org_name.strip():
                raise ValueError(f"NAME_MISMATCH: ABR entity name '{abr_name}' must match organisation name '{org_name}'")
        
        # Individual name consistency with ABR entity
        if self.individual and self.abrEntity and self.ownerType == OwnerType.IND:
            given_names = self.individual.name.givenNames
            family_name = self.individual.name.familyName
            full_name = f"{given_names} {family_name}".strip()
            
            abr_name = self.abrEntity.entityName
            
            if full_name and abr_name and full_name != abr_name.strip():
                raise ValueError(f"INDIVIDUAL_NAME_MISMATCH: Individual name '{full_name}' must match ABR entity name '{abr_name}'")
        
        return self
    
    def get_partner_classification_summary(self) -> dict:
        """Get summary of partner classifications (useful for debugging/reporting)"""
        if not self.associate:
            return {"total_partners": 0}
        
        summary = {
            "total_partners": len(self.associate),
            "individual_partners": 0,
            "incorporated_partners": 0,
            "unincorporated_partners": 0,
            "unincorporated_details": []
        }
        
        for i, partner in enumerate(self.associate):
            classification = partner.partner_classification
            
            if classification == "individual":
                summary["individual_partners"] += 1
            elif classification == "incorporated":
                summary["incorporated_partners"] += 1
            elif classification == "unincorporated":
                summary["unincorporated_partners"] += 1
                summary["unincorporated_details"].append({
                    "partner_index": i,
                    "partner_name": partner.get_primary_name(),
                    "representatives": partner.get_representative_summary()
                })
        
        return summary
    
    def get_validation_summary(self) -> dict:
        """Get a summary of validation requirements for this owner type"""
        base_summary = {
            'owner_type': self.ownerType.value,
            'requires_individual': self.ownerType == OwnerType.IND,
            'requires_organisation': self.ownerType != OwnerType.IND,
            'requires_associates': self.ownerType in [OwnerType.PTSH, OwnerType.USTR, OwnerType.JV],
            'requires_acn': self.ownerType == OwnerType.IB,
            'allows_abn_exemption': self.ownerType == OwnerType.JV
        }
        
        # Add partner classification summary for complex owner types
        if self.ownerType in [OwnerType.PTSH, OwnerType.JV]:
            base_summary['partner_classification'] = self.get_partner_classification_summary()
        
        return base_summary
