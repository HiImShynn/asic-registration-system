from typing import Literal
from decouple import config
from apps.common.models import ASICBaseModel

class QueryNameAvailabilityHeaders(ASICBaseModel):
    """Headers for query name availability requests"""
    messageType: Literal["queryNameAvailability"] = "queryNameAvailability"
    messageVersion: Literal[2] = 2
    senderType: str = str(config("ASIC_SENDER_TYPE", default="REGA"))
    senderId: str = str(config("ASIC_SENDER_ID", default="000040540"))

class SearchNniNameHeaders(ASICBaseModel):
    """Headers for search NNI name requests"""
    messageType: Literal["searchNniName"] = "searchNniName"
    messageVersion: Literal[3] = 3
    senderType: str = str(config("ASIC_SENDER_TYPE", default="REGA"))
    senderId: str = str(config("ASIC_SENDER_ID", default="000040540"))

class GetNniHeaders(ASICBaseModel):
    """Headers for get NNI requests"""
    messageType: Literal["getNni"] = "getNni"
    messageVersion: Literal[3] = 3
    senderType: str = str(config("ASIC_SENDER_TYPE", default="REGA"))
    senderId: str = str(config("ASIC_SENDER_ID", default="000040540"))

class QueryAddressHeaders(ASICBaseModel):
    """Headers for query address requests"""
    messageType: Literal["queryAddress"] = "queryAddress"
    messageVersion: Literal[1] = 1
    senderType: str = str(config("ASIC_SENDER_TYPE", default="REGA"))
    senderId: str = str(config("ASIC_SENDER_ID", default="000040540"))

class BnLodgeApplicationHeaders(ASICBaseModel):
    """Headers for BN lodge application requests"""
    messageType: Literal["bnLodgeApplication"] = "bnLodgeApplication"
    messageVersion: Literal[1] = 1
    senderType: str = str(config("ASIC_SENDER_TYPE", default="REGA"))
    senderId: str = str(config("ASIC_SENDER_ID", default="000040540"))

