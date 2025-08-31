from enum import Enum
from typing import Optional, List, Dict, Any

class SearchType(str, Enum):
    """Search type options for ASIC name searches"""
    STANDARD = "S"
    EXACT = "E"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class SearchScope(str, Enum):
    """Search scopes for ASIC searchNniName"""
    NAMES_VALID_FOR_EXTRACT = "1"
    CURRENT_NAMES_AND_RESERVATIONS = "2"
    INCLUDE_DEREGISTERED = "3"
    ALL_ENTITIES = "A"
    BUSINESS_NAMES_AND_STATE = "B"
    REG_DEREG_COMPANIES_TRUSTS_NRETS = "C"
    REGISTERED_COMPANIES_AND_NRETS = "E"
    FULL_SCOPE_WITH_BUSN_AND_STATE = "G"
    EXTENDED_SCOPE_WITH_DEREGISTERED = "H"
    NONC_REGISTERED_TRUSTS_NRETS = "I"
    COMPANIES_AND_RESERVATIONS = "J"
    NONC_AND_BUSINESS_NAMES = "L"
    NONC_AND_RESERVATIONS = "M"
    NON_COMPANY_NAMES = "N"
    NONC_AND_REGISTERED_COMPANIES = "O"
    TRUSTS_AND_SCHEMES = "T"
    REGISTERED_COMPANIES = "R"
    COMBINED_STANDARD_SCOPE = "S"
    CURRENT_NAME_RESERVATIONS = "P"
    COMPANIES_RESERVATIONS_BUSN = "X"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class EntityType(str, Enum):
    """ASIC organisation type codes"""
    PROPRIETARY_COMPANY = "APTY"
    PUBLIC_COMPANY = "APUB"
    PASSPORT_FUND_AU = "ARPA"
    PASSPORT_FUND_FOREIGN = "ARPF"
    ASSOCIATION = "ASSN"
    BUSINESS_NAME = "BUSN"
    CHARITY = "CHAR"
    COMMUNITY_PURPOSE = "COMP"
    COOPERATIVE = "COOP"
    FOREIGN_COMPANY = "FNOS"
    LIMITED_PARTNERSHIP = "LTDP"
    MANAGED_INVESTMENT_SCHEME = "MISM"
    NON_COMPANY = "NONC"
    NON_REGISTERED_ENTITY = "NRET"
    REGISTERED_AUSTRALIAN_BODY = "RACN"
    RELIGIOUS_BODY = "REBD"
    NAME_RESERVATION = "RSVN"
    SOLICITOR_CORPORATION = "SOLS"
    TRUST = "TRST"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class EntityStatus(str, Enum):
    """Business name registration status"""
    REGISTERED = "REGD"
    CANCELLED = "DRGD"
    PENDING = "PEND"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class TermType(str, Enum):
    """Business name registration term options"""
    ONE_YEAR = "1"
    THREE_YEARS = "3"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class AddressTypeType(str, Enum):
    """Address type codes for ASIC"""
    REGISTERED_OFFICE_COMPANY = "RG"
    REGISTERED_OFFICE_FOREIGN_COMPANY = "RP"
    PRINCIPAL_PLACE_OF_BUSINESS_ADDRESS_COMPANY = "PA"
    REGISTERED_OFFICE_IN_PLACE_OF_INCORPORATION_FOREIGN_COMPANY = "RO"
    RESIDENTIAL_ADDRESS_BUSINESS_NAMES = "GC"
    ADDRESS_FOR_THE_PLACE_OF_BUSINESS_BUSINESS_NAMES = "GD"
    ADDRESS_FOR_THE_SERVICE_OF_DOCUMENTS_BUSINESS_NAMES = "GE"
    CONTACT_ADDRESS_BUSINESS_NAMES = "GL"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class StatusType(str, Enum):
    """Status codes for entities in ASIC"""
    PENDING_REGISTRATION = "PEND"
    REGISTERED = "REGD"
    DEREGISTERED = "DRGD"
    HELD = "HELD"
    STRIKE_OFF = "SOFF"
    UNDER_EXTERNAL_ADMINISTRATION_CONTROLLER_APPOINTED = "EXAD"
    CANCELLED = "CNCL"
    NOT_REGISTERED = "NRGD"
    DORMANT = "DMNT"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class PostalDeliveryType(str, Enum):
    """Postal delivery type codes"""
    CARE_OF_POST_OFFICE_POSTE_RESTANTE = "CARE_PO"
    COMMUNITY_MAIL_AGENT = "CMA"
    COMMUNITY_MAIL_BAG = "CMB"
    GENERAL_POST_OFFICE_BOX_POSTALDELIVERYNUMBER_REQUIRED = "GPO_BOX"
    LOCKED_MAIL_BAG_SERVICE_POSTALDELIVERYNUMBER_REQUIRED = "LOCKED_BAG"
    MAIL_SERVICE = "MS"
    POST_OFFICE_BOX_POSTALDELIVERYNUMBER_REQUIRED = "PO_BOX"
    PRIVATE_MAIL_BAG_SERVICE_POSTALDELIVERYNUMBER_REQUIRED = "PRIVATE_BAG"
    ROADSIDE_DELIVERY = "RSD"
    ROADSIDE_MAIL_BAG_BOX_POSTALDELIVERYNUMBER_REQUIRED = "RMB"
    ROADSIDE_MAIL_SERVICE = "RMS"
    COMMUNITY_POSTAL_AGENT = "CPA"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class StateTerritoryCodeType(str, Enum):
    """Australian state and territory codes"""
    AUSTRALIAN_CAPITAL_TERRITORY = "ACT"
    COCOS_KEELING_ISLANDS = "CCK"
    CHRISTMAS_ISLAND = "CXR"
    JERVIS_BAY_TERRITORY = "JBT"
    NEW_SOUTH_WALES = "NSW"
    NORFOLK_ISLAND = "NFK"
    NORTHERN_TERRITORY = "NT"
    QUEENSLAND = "QLD"
    SOUTH_AUSTRALIA = "SA"
    TASMANIA = "TAS"
    VICTORIA = "VIC"
    WESTERN_AUSTRALIA = "WA"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class ASICEntityType(str, Enum):
    """ASIC entity type classifications"""
    INCORPORATED_BODY = "IB"
    UNINCORPORATED = "USTR"
    INDIVIDUAL = "IND"
    PARTNERSHIP = "PTSH"
    JOINT_VENTURE = "JV"
    CONDITIONAL = "COND"

    @classmethod
    def as_choices(cls) -> List[Dict[str, str]]:
        return [
            {"value": member.value, "label": member.name.replace("_", " ").title()}
            for member in cls
        ]

class ABREntityType(str, Enum):
    """ABR entity type codes"""
    # Incorporated body
    AUSTRALIAN_PRIVATE_COMPANY = 'PRV'
    AUSTRALIAN_PUBLIC_COMPANY = 'PUB'
    AUSTRALIAN_PRIVATE_COMPANY_COMMONWEALTH = 'CCR'
    AUSTRALIAN_PRIVATE_COMPANY_LOCAL = 'LCR'
    AUSTRALIAN_PRIVATE_COMPANY_STATE = 'SCR'
    AUSTRALIAN_PRIVATE_COMPANY_TERRITORY = 'TCR'
    AUSTRALIAN_PUBLIC_COMPANY_COMMONWEALTH = 'CCB'
    AUSTRALIAN_PUBLIC_COMPANY_LOCAL = 'LCB'
    AUSTRALIAN_PUBLIC_COMPANY_STATE = 'SCB'
    AUSTRALIAN_PUBLIC_COMPANY_TERRITORY = 'TCB'
    POOLED_DEVELOPMENT_FUND = 'PDF'
    POOLED_DEVELOPMENT_FUND_COMMONWEALTH = 'CCP'
    POOLED_DEVELOPMENT_FUND_LOCAL = 'LCP'
    POOLED_DEVELOPMENT_FUND_STATE = 'SCP'
    POOLED_DEVELOPMENT_FUND_TERRITORY = 'TCP'
    # Individual
    INDIVIDUAL = 'IND'
    # Partnerships
    FAMILY_PARTNERSHIP = 'FPT'
    LIMITED_PARTNERSHIP = 'LPT'
    OTHER_PARTNERSHIP = 'PTR'
    LIMITED_PARTNERSHIP_LOCAL = 'LCL'
    LIMITED_PARTNERSHIP_STATE = 'SCL'
    LIMITED_PARTNERSHIP_TERRITORY = 'TCL'
    OTHER_PARTNERSHIP_COMMONWEALTH = 'CGP'
    OTHER_PARTNERSHIP_LOCAL = 'LGP'
    OTHER_PARTNERSHIP_STATE = 'SGP'
    OTHER_PARTNERSHIP_TERRITORY = 'TGP'
    # Unincorporated entities
    APPROVED_DEPOSIT_FUND = 'ADF'
    APRA_REGULATED_FUND_FUND_TYPE_UNKNOWN = 'ARF'
    CO_OPERATIVE_COMMONWEALTH = 'CCC'
    OTHER_UNINCORPORATED_ENTITY_COMMONWEALTH = 'CCN'
    CORPORATE_UNIT_TRUST_COMMONWEALTH = 'CCU'
    COMMONWEALTH_GOVERNMENT_STATUTORY__AUTHORITY = 'CGA'
    COMMONWEALTH_GOVERNMENT_COMPANY = 'CGC'
    COMMONWEALTH_GOVERNMENT_ENTITY = 'CGE'
    COMMONWEALTH_GOVERNMENT_SUPERANNUATION_FUND = 'CGS'
    COMMONWEALTH_GOVERNMENT_TRUST = 'CGT'
    CASH_MANAGEMENT_TRUST = 'CMT'
    CO_OPERATIVE = 'COP'
    APRA_REGULATED_SUPER_FUND_COMMONWEALTH_PUBLIC_SECTOR_FUND = 'CSA'
    APRA_REGULATED_SUPER_FUND_COMMONWEALTH_PUBLIC_SECTOR_SCHEME = 'CSP'
    A_NON_REGULATED_SUPERANNUATION_FUND_COMMONWEALTH = 'CSS'
    CASH_MANAGEMENT_TRUST_COMMONWEALTH = 'CTC'
    DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_COMMONWEALTH = 'CTD'
    FIXED_TRUST_COMMONWEALTH = 'CTF'
    HYBRID_TRUST_COMMONWEALTH = 'CTH'
    DISCRETIONARY_TRUST_INVESTMENT_COMMONWEALTH = 'CTI'
    PUBLIC_UNIT_TRUST_LISTED_COMMONWEALTH = 'CTL'
    PUBLIC_UNIT_TRUST_UNLISTED_COMMONWEALTH = 'CTQ'
    DISCRETIONARY_TRUST_TRADING_COMMONWEALTH = 'CTT'
    FIXED_UNIT_TRUST_COMMONWEALTH = 'CTU'
    CORPORATE_UNIT_TRUST = 'CUT'
    DECEASED_ESTATE = 'DES'
    DIPLOMATIC_CONSULATE_BODY_OR_HIGH_COMMISSIONER = 'DIP'
    DISCRETIONARY_INVESTMENT_TRUST = 'DIT'
    DISCRETIONARY_SERVICE_MANAGEMENT_TRUST = 'DST'
    DISCRETIONARY_TRADING_TRUST = 'DTT'
    FIRST_HOME_SAVER_ACCOUNT_FHSA_TRUST = 'FHS'
    FIXED_UNIT_TRUST = 'FUT'
    FIXED_TRUST = 'FXT'
    HYBRID_TRUST = 'HYT'
    CO_OPERATIVE_LOCAL = 'LCC'
    OTHER_UNINCORPORATED_ENTITY_LOCAL = 'LCN'
    CORPORATE_UNIT_TRUST_LOCAL = 'LCU'
    LOCAL_GOVERNMENT_STATUTORY_AUTHORITY = 'LGA'
    LOCAL_GOVERNMENT_COMPANY = 'LGC'
    LOCAL_GOVERNMENT_ENTITY = 'LGE'
    LOCAL_GOVERNMENT_TRUST = 'LGT'
    APRA_REGULATED_SUPER_FUND_LOCAL_PUBLIC_SECTOR_FUND = 'LSA'
    APRA_REGULATED_SUPER_FUND_LOCAL_PUBLIC_SECTOR_SCHEME = 'LSP'
    A_NON_REGULATED_SUPERANNUATION_FUND_LOCAL = 'LSS'
    CASH_MANAGEMENT_TRUST_LOCAL = 'LTC'
    DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_LOCAL = 'LTD'
    FIXED_TRUST_LOCAL = 'LTF'
    HYBRID_TRUST_LOCAL = 'LTH'
    DISCRETIONARY_TRUST_INVESTMENT_LOCAL = 'LTI'
    PUBLIC_UNIT_TRUST_LISTED_LOCAL = 'LTL'
    PUBLIC_UNIT_TRUST_UNLISTED_LOCAL = 'LTQ'
    DISCRETIONARY_TRUST_TRADING_LOCAL = 'LTT'
    FIXED_UNIT_TRUST_LOCAL = 'LTU'
    APRA_REGULATED_NON_PUBLIC_OFFER_FUND = 'NPF'
    NON_REGULATED_SUPERANNUATION_FUND = 'NRF'
    APRA_REGULATED_PUBLIC_OFFER_FUND = 'POF'
    UNLISTED_PUBLIC_UNIT_TRUST = 'PQT'
    POOLED_SUPERANNUATION_TRUST = 'PST'
    LISTED_PUBLIC_UNIT_TRUST = 'PUT'
    SMALL_APRA_REGULATED_FUND = 'SAF'
    CO_OPERATIVE_STATE = 'SCC'
    OTHER_UNINCORPORATED_ENTITY_STATE = 'SCN'
    CORPORATE_UNIT_TRUST_STATE = 'SCU'
    STATE_GOVERNMENT_STATUTORY_AUTHORITY = 'SGA'
    STATE_GOVERNMENT_COMPANY = 'SGC'
    STATE_GOVERNMENT_ENTITY = 'SGE'
    STATE_GOVERNMENT_TRUST = 'SGT'
    AN_ATO_REGULATED_SELF_MANAGED_SUPERANNUATION_FUND = 'SMF'
    APRA_REGULATED_SUPER_FUND_STATE_PUBLIC_SECTOR_FUND = 'SSA'
    APRA_REGULATED_SUPER_FUND_STATE_PUBLIC_SECTOR_SCHEME = 'SSP'
    A_NON_REGULATED_SUPERANNUATION_FUND_STATE = 'SSS'
    CASH_MANAGEMENT_TRUST_STATE = 'STC'
    DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_STATE = 'STD'
    FIXED_TRUST_STATE = 'STF'
    HYBRID_TRUST_STATE = 'STH'
    DISCRETIONARY_TRUST_INVESTMENT_STATE = 'STI'
    PUBLIC_UNIT_TRUST_LISTED_STATE = 'STL'
    PUBLIC_UNIT_TRUST_UNLISTED_STATE = 'STQ'
    DISCRETIONARY_TRUST_TRADING_STATE = 'STT'
    FIXED_UNIT_TRUST_STATE = 'STU'
    SUPER_FUND = 'SUP'
    CO_OPERATIVE_TERRITORY = 'TCC'
    OTHER_UNINCORPORATED_ENTITY_TERRITORY = 'TCN'
    CORPORATE_UNIT_TRUST_TERRITORY = 'TCU'
    TERRITORY_GOVERNMENT_STATUTORY_AUTHORITY = 'TGA'
    TERRITORY_GOVERNMENT_ENTITY = 'TGE'
    TERRITORY_GOVERNMENT_TRUST = 'TGT'
    OTHER_TRUST = 'TRT'
    APRA_REGULATED_SUPER_FUND_TERRITORY_PUBLIC_SECTOR_FUND = 'TSA'
    APRA_REGULATED_SUPER_FUND_TERRITORY_PUBLIC_SECTOR_SCHEME = 'TSP'
    A_NON_REGULATED_SUPERANNUATION_FUND_TERRITORY = 'TSS'
    CASH_MANAGEMENT_TRUST_TERRITORY = 'TTC'
    DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_TERRITORY = 'TTD'
    FIXED_TRUST_TERRITORY = 'TTF'
    HYBRID_TRUST_TERRITORY = 'TTH'
    DISCRETIONARY_TRUST_INVESTMENT_TERRITORY = 'TTI'
    PUBLIC_UNIT_TRUST_LISTED_TERRITORY = 'TTL'
    PUBLIC_UNIT_TRUST_UNLISTED_TERRITORY = 'TTQ'
    DISCRETIONARY_TRUST_TRADING_TERRITORY = 'TTT'
    FIXED_UNIT_TRUST_TERRITORY = 'TTU'
    OTHER_UNINCORPORATED_ENTITY = 'UIE'
    # Conditional entities
    OTHER_INCORPORATED_ENTITY = 'OIE'
    OTHER_INCORPORATED_ENTITY_COMMONWEALTH = 'CCO'
    OTHER_INCORPORATED_ENTITY_LOCAL = 'LCO'
    OTHER_INCORPORATED_ENTITY_STATE = 'SCO'
    OTHER_INCORPORATED_ENTITY_TERRITORY = 'TCO'
    STRATA_TITLE_COMMONWEALTH = 'CCS'
    PUBLIC_TRADING_TRUST_COMMONWEALTH = 'CCT'
    STRATA_TITLE_LOCAL = 'LCS'
    PUBLIC_TRADING_TRUST_LOCAL = 'LCT'
    PUBLIC_TRADING_TRUST = 'PTT'
    STRATA_TITLE_STATE = 'SCS'
    PUBLIC_TRADING_TRUST_STATE = 'SCT'
    STRATA_TITLE = 'STR'
    STRATA_TITLE_TERRITORY = 'TCS'
    PUBLIC_TRADING_TRUST_TERRITORY = 'TCT'

# Constants
STREET_TYPES = [
    'Accs', 'Cres', 'Gdns', 'Pkwy', 'Spur', 
    'Ally', 'Cres E', 'Gld', 'Pl', 'Sq', 
    'Ambl', 'Cres N', 'Glen', 'Pl E', 'Sq E', 
    'App', 'Cres S', 'Gly', 'Pl N', 'Sq N', 
    'Arc', 'Cres W', 'Gr', 'Pl S', 'Sq S', 
    'Art', 'Crs', 'Gr E', 'Pl W', 'Sq W', 
    'Ave', 'Crss', 'Gr N', 'Plza', 'St', 
    'Ave Cn', 'Crss W', 'GrS', 'Pnt', 'St Cn', 
    'Ave E', 'Crst', 'Gra', 'Port', 'St E', 
    'Ave Ex', 'CSO', 'Grn', 'Prom', 'St Ex',
    'Ave N', 'Ct', 'Gte', 'Qdrt', 'St N', 
    'Ave S', 'Ct E', 'Hill', 'Quad', 'St S', 
    'Ave W', 'Ct N', 'Hts', 'Qy', 'St W', 
    'Bch', 'Cts', 'Hwy', 'Qy E', 'Stps', 
    'Bdwy', 'Ct W', 'Hwy E', 'Qy W', 'Strp', 
    'Bend', 'Ctr', 'Hwy N', 'Qys', 'Tarn', 
    'Brae', 'Cttg', 'Hwy S', 'Ramp', 'Tce', 
    'Brce', 'Ctyd', 'Hwy W', 'Rch', 'Tce E', 
    'Brk', 'Dale', 'Jnc', 'Rd', 'Tce Ex', 
    'Brow', 'Dell', 'Key', 'Rd Cn', 'Tce N', 
    'Bvd', 'Devn', 'Lane', 'Rd E', 'Tce S', 
    'Bvd E', 'Dr', 'Lane E', 'Rd Ex', 'Tce W',
    'Bvd S', 'Dr E', 'Lane N', 'Rd Lr', 'Top', 
    'Bvd W', 'Dr N', 'Lane S', 'Rd N', 'Tor', 
    'Bypa', 'Dr S', 'Lane W', 'Rd S', 'Trk', 
    'Caus', 'Dr W', 'Line', 'Rd W', 'Trk E', 
    'Cct', 'Drwy', 'Link', 'Rdge', 'Trl', 
    'Cct E', 'Edge', 'Lkt', 'Rds', 'Turn', 
    'Cct W', 'Elb', 'Lnwy', 'Rdwy', 'Vale', 
    'Ch', 'End', 'Loop', 'Res', 'View', 
    'Cir', 'Ent', 'Mall', 'Rest', 'Vsta', 
    'Cir N', 'Esp', 'Mews', 'Ride', 'Walk', 
    'Cir S', 'Esp N', 'Mndr', 'Ring', 'Walk N', 
    'Cl', 'Esp S', 'Mwy', 'Rise', 'Walk S', 
    'Cl N', 'Est', 'Nook', 'Rmbl', 'Way', 
    'Cl S', 'Fawy', 'Otlk', 'Rnd', 'Way E', 
    'Clt', 'Fitr', 'Park', 'Rnge', 'Way N', 
    'Cmmn', 'Flat', 'Pass', 'Row', 'Way S', 
    'Cnr', 'Folw', 'Path', 'Rte', 'Way W', 
    'Con', 'Frnt', 'Pde', 'Rtt', 'Whrf', 
    'Cove', 'Frtg', 'Pde E', 'Run', 'Wkwy', 
    'Cps', 'Fshr', 'Pde N', 'Rvr', 'Wynd', 
    'Crcs', 'Ftrk', 'Pde S', 'SWy', 'Crcs E', 
    'Fwy', 'Pde W', 'Sbwy', 'Crcs W', 'Gap', 
    'Pkt', 'Slpe'
]

COUNTRY = [
    "Afghanistan", "Aland Islands", "Albania", "Algeria",
    "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica",
    "Antigua And Barbuda", "Argentina", "Armenia", "Aruba", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
    "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bermuda", "Bhutan", "Bolivia", "Bonaire, Sint Eustatius And Saba", "Bosnia And Herzegovina",
    "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon",
    "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad",
    "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia",
    "Comoros", "Congo", "Congo, The Democratic Republic Of The", "Cook Islands", "Costa Rica",
    "Cote D'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus",
    "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
    "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji",
    "Finland", "France", "French Guiana", "French Polynesia", "French Southern Territories",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
    "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe",
    "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Heard Island And Mcdonald Islands", "Holy See (Vatican City State)", "Honduras",
    "Hong Kong", "Hungary", "Iceland", "India", "Indonesia",
    "Iran, Islamic Republic Of", "Iraq", "Ireland", "Isle Of Man", "Israel",
    "Italy", "Jamaica", "Japan", "Jersey", "Jordan",
    "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic Of", "Korea, Republic Of",
    "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania",
    "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
    "Micronesia", "Moldova, Republic Of", "Monaco", "Mongolia", "Montenegro",
    "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island",
    "Northern Ireland", "Northern Mariana Islands", "Norway", "Oman", "Pakistan",
    "Palau", "Palestinian Territory, OCC", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Pitcairn", "Poland", "Portugal",
    "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation",
    "Rwanda", "Saint Barthelemy", "Saint Helena, Ascension and Tristan Da Cunha", "Saint Kitts And Nevis", "Saint Lucia",
    "Saint Martin (French Part)", "Saint Pierre And Miquelon", "Saint Vincent And The Grenadines", "Samoa", "San Marino",
    "Sao Tome And Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Sint Maarten (Dutch Part)", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Svalbard And Jan Mayen", "Swaziland",
    "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan",
    "Tanzania, United Republic Of", "Thailand", "Timor-Leste", "Togo", "Tokelau",
    "Tonga", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan",
    "Turks And Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States", "United States Minor Outlying Islands", "Unknown", "Uruguay",
    "Uzbekistan", "Vanuatu", "Venezuela, Bolivarian Republic", "Viet Nam", "Virgin Islands, British",
    "Virgin Islands, U.S.", "Wallis And Futuna", "Western Sahara", "Yemen", "Zambia",
    "Zimbabwe",
]

# Mapping ABREntityType to ASICEntityType
ABR_TO_ASIC_MAP = {
    # Incorporated body
    ABREntityType.AUSTRALIAN_PRIVATE_COMPANY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PUBLIC_COMPANY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PRIVATE_COMPANY_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PRIVATE_COMPANY_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PRIVATE_COMPANY_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PRIVATE_COMPANY_TERRITORY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PUBLIC_COMPANY_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PUBLIC_COMPANY_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PUBLIC_COMPANY_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.AUSTRALIAN_PUBLIC_COMPANY_TERRITORY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.POOLED_DEVELOPMENT_FUND: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.POOLED_DEVELOPMENT_FUND_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.POOLED_DEVELOPMENT_FUND_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.POOLED_DEVELOPMENT_FUND_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.POOLED_DEVELOPMENT_FUND_TERRITORY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.OTHER_INCORPORATED_ENTITY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.OTHER_INCORPORATED_ENTITY_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.OTHER_INCORPORATED_ENTITY_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.OTHER_INCORPORATED_ENTITY_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.OTHER_INCORPORATED_ENTITY_TERRITORY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.STRATA_TITLE_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.STRATA_TITLE_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.STRATA_TITLE_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.STRATA_TITLE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.STRATA_TITLE_TERRITORY: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.PUBLIC_TRADING_TRUST_COMMONWEALTH: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.PUBLIC_TRADING_TRUST_LOCAL: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.PUBLIC_TRADING_TRUST: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.PUBLIC_TRADING_TRUST_STATE: ASICEntityType.INCORPORATED_BODY,
    ABREntityType.PUBLIC_TRADING_TRUST_TERRITORY: ASICEntityType.INCORPORATED_BODY,

    # Individual
    ABREntityType.INDIVIDUAL: ASICEntityType.INDIVIDUAL,

    # Partnerships
    ABREntityType.FAMILY_PARTNERSHIP: ASICEntityType.PARTNERSHIP,
    ABREntityType.LIMITED_PARTNERSHIP: ASICEntityType.PARTNERSHIP,
    ABREntityType.OTHER_PARTNERSHIP: ASICEntityType.PARTNERSHIP,
    ABREntityType.LIMITED_PARTNERSHIP_LOCAL: ASICEntityType.PARTNERSHIP,
    ABREntityType.LIMITED_PARTNERSHIP_STATE: ASICEntityType.PARTNERSHIP,
    ABREntityType.LIMITED_PARTNERSHIP_TERRITORY: ASICEntityType.PARTNERSHIP,
    ABREntityType.OTHER_PARTNERSHIP_COMMONWEALTH: ASICEntityType.PARTNERSHIP,
    ABREntityType.OTHER_PARTNERSHIP_LOCAL: ASICEntityType.PARTNERSHIP,
    ABREntityType.OTHER_PARTNERSHIP_STATE: ASICEntityType.PARTNERSHIP,
    ABREntityType.OTHER_PARTNERSHIP_TERRITORY: ASICEntityType.PARTNERSHIP,

    # Unincorporated entities
    ABREntityType.APPROVED_DEPOSIT_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_FUND_FUND_TYPE_UNKNOWN: ASICEntityType.UNINCORPORATED,
    ABREntityType.CO_OPERATIVE_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_UNINCORPORATED_ENTITY_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.CORPORATE_UNIT_TRUST_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.COMMONWEALTH_GOVERNMENT_STATUTORY__AUTHORITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.COMMONWEALTH_GOVERNMENT_COMPANY: ASICEntityType.UNINCORPORATED,
    ABREntityType.COMMONWEALTH_GOVERNMENT_ENTITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.COMMONWEALTH_GOVERNMENT_SUPERANNUATION_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.COMMONWEALTH_GOVERNMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.CASH_MANAGEMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.CO_OPERATIVE: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_COMMONWEALTH_PUBLIC_SECTOR_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_COMMONWEALTH_PUBLIC_SECTOR_SCHEME: ASICEntityType.UNINCORPORATED,
    ABREntityType.A_NON_REGULATED_SUPERANNUATION_FUND_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.CASH_MANAGEMENT_TRUST_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_TRUST_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.HYBRID_TRUST_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_INVESTMENT_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_LISTED_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_UNLISTED_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_TRADING_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_UNIT_TRUST_COMMONWEALTH: ASICEntityType.UNINCORPORATED,
    ABREntityType.CORPORATE_UNIT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.DECEASED_ESTATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.DIPLOMATIC_CONSULATE_BODY_OR_HIGH_COMMISSIONER: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_INVESTMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_SERVICE_MANAGEMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRADING_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIRST_HOME_SAVER_ACCOUNT_FHSA_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_UNIT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.HYBRID_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.CO_OPERATIVE_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_UNINCORPORATED_ENTITY_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.CORPORATE_UNIT_TRUST_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.LOCAL_GOVERNMENT_STATUTORY_AUTHORITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.LOCAL_GOVERNMENT_COMPANY: ASICEntityType.UNINCORPORATED,
    ABREntityType.LOCAL_GOVERNMENT_ENTITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.LOCAL_GOVERNMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_LOCAL_PUBLIC_SECTOR_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_LOCAL_PUBLIC_SECTOR_SCHEME: ASICEntityType.UNINCORPORATED,
    ABREntityType.A_NON_REGULATED_SUPERANNUATION_FUND_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.CASH_MANAGEMENT_TRUST_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_TRUST_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.HYBRID_TRUST_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_INVESTMENT_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_LISTED_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_UNLISTED_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_TRADING_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_UNIT_TRUST_LOCAL: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_NON_PUBLIC_OFFER_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.NON_REGULATED_SUPERANNUATION_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_PUBLIC_OFFER_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.UNLISTED_PUBLIC_UNIT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.POOLED_SUPERANNUATION_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.LISTED_PUBLIC_UNIT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.SMALL_APRA_REGULATED_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.CO_OPERATIVE_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_UNINCORPORATED_ENTITY_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.CORPORATE_UNIT_TRUST_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.STATE_GOVERNMENT_STATUTORY_AUTHORITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.STATE_GOVERNMENT_COMPANY: ASICEntityType.UNINCORPORATED,
    ABREntityType.STATE_GOVERNMENT_ENTITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.STATE_GOVERNMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.AN_ATO_REGULATED_SELF_MANAGED_SUPERANNUATION_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_STATE_PUBLIC_SECTOR_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_STATE_PUBLIC_SECTOR_SCHEME: ASICEntityType.UNINCORPORATED,
    ABREntityType.A_NON_REGULATED_SUPERANNUATION_FUND_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.CASH_MANAGEMENT_TRUST_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_TRUST_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.HYBRID_TRUST_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_INVESTMENT_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_LISTED_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_UNLISTED_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_TRADING_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_UNIT_TRUST_STATE: ASICEntityType.UNINCORPORATED,
    ABREntityType.SUPER_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.CO_OPERATIVE_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_UNINCORPORATED_ENTITY_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.CORPORATE_UNIT_TRUST_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.TERRITORY_GOVERNMENT_STATUTORY_AUTHORITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.TERRITORY_GOVERNMENT_ENTITY: ASICEntityType.UNINCORPORATED,
    ABREntityType.TERRITORY_GOVERNMENT_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_TRUST: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_TERRITORY_PUBLIC_SECTOR_FUND: ASICEntityType.UNINCORPORATED,
    ABREntityType.APRA_REGULATED_SUPER_FUND_TERRITORY_PUBLIC_SECTOR_SCHEME: ASICEntityType.UNINCORPORATED,
    ABREntityType.A_NON_REGULATED_SUPERANNUATION_FUND_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.CASH_MANAGEMENT_TRUST_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_SERVICES_MANAGEMENT_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_TRUST_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.HYBRID_TRUST_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_INVESTMENT_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_LISTED_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.PUBLIC_UNIT_TRUST_UNLISTED_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.DISCRETIONARY_TRUST_TRADING_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.FIXED_UNIT_TRUST_TERRITORY: ASICEntityType.UNINCORPORATED,
    ABREntityType.OTHER_UNINCORPORATED_ENTITY: ASICEntityType.UNINCORPORATED,
    # Conditional entities
    ABREntityType.OTHER_INCORPORATED_ENTITY: ASICEntityType.CONDITIONAL,
    ABREntityType.OTHER_INCORPORATED_ENTITY_COMMONWEALTH: ASICEntityType.CONDITIONAL,
    ABREntityType.OTHER_INCORPORATED_ENTITY_LOCAL: ASICEntityType.CONDITIONAL,
    ABREntityType.OTHER_INCORPORATED_ENTITY_STATE: ASICEntityType.CONDITIONAL,
    ABREntityType.OTHER_INCORPORATED_ENTITY_TERRITORY: ASICEntityType.CONDITIONAL,
    ABREntityType.STRATA_TITLE_COMMONWEALTH: ASICEntityType.CONDITIONAL,
    ABREntityType.PUBLIC_TRADING_TRUST_COMMONWEALTH: ASICEntityType.CONDITIONAL,
    ABREntityType.STRATA_TITLE_LOCAL: ASICEntityType.CONDITIONAL,
    ABREntityType.PUBLIC_TRADING_TRUST_LOCAL: ASICEntityType.CONDITIONAL,
    ABREntityType.PUBLIC_TRADING_TRUST: ASICEntityType.CONDITIONAL,
    ABREntityType.STRATA_TITLE_STATE: ASICEntityType.CONDITIONAL,
    ABREntityType.PUBLIC_TRADING_TRUST_STATE: ASICEntityType.CONDITIONAL,
    ABREntityType.STRATA_TITLE: ASICEntityType.CONDITIONAL,
    ABREntityType.STRATA_TITLE_TERRITORY: ASICEntityType.CONDITIONAL,
    ABREntityType.PUBLIC_TRADING_TRUST_TERRITORY: ASICEntityType.CONDITIONAL,
}

class BusinessEntityClassifier:
    @staticmethod
    def classify(abr_code: str, asic_id: Optional[str]) -> ASICEntityType:
        """
        Classify an entity based on ABR code and ASIC ID
        
        Args:
            abr_code: The ABR entity type code
            asic_id: The ASIC identifier, if available
            
        Returns:
            The appropriate ASICEntityType classification
        """
        abr_enum = ABREntityType(abr_code)
        base_type = ABR_TO_ASIC_MAP.get(abr_enum)
        if base_type == ASICEntityType.CONDITIONAL:
            return ASICEntityType.INCORPORATED_BODY if asic_id else ASICEntityType.UNINCORPORATED
        if base_type is None:
            raise ValueError(f"Unknown ABR entity type code: {abr_code}")
        return base_type

