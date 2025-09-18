from apps.common.enums.asic_enums import SearchType, SearchScope, EntityType, StatusType
from apps.common.models import ASICBaseModel
from typing import Optional, List, Annotated
from pydantic import Field

class SearchNniOrganisation(ASICBaseModel):
    """Organisation details for search NNI"""
    name: Annotated[str, Field(min_length=1, max_length=200, description="The name of the organisation")]
    type: Optional[Annotated[EntityType, Field(description="The type of the organisation")]] = None
    status: Optional[Annotated[StatusType, Field(description="The status of the organisation")]] = None

class SearchNniBody(ASICBaseModel):
    """Request body for search NNI name"""
    searchType: Annotated[SearchType, Field(description="The type of search to perform", default=SearchType.STANDARD)]
    searchScope: Annotated[SearchScope, Field(description="The scope of the search", default=SearchScope.ALL_ENTITIES)]
    organisation: Annotated[SearchNniOrganisation, Field(description="The organisation details to search for")]
    maxResults: Optional[Annotated[int, Field(gt=0, le=100, description="Maximum number of results to return (1-100)")]] = 10
