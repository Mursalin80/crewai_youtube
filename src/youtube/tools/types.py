from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone



# Inputs
class AddVideoToVectorDB_Input(BaseModel):
    """Input for FetchLatestVideosForChannel."""

    video_url: str = Field(
        ..., description="The URL of the YouTube video to add to the vector DB."
    )

class FetchLatestVideosFromYouTubeChannel_Input(BaseModel):
    """Input for FetchLatestVideosFromYouTubeChannel."""

    youtube_channel_handle: str = Field(
        ..., description="The YouTube channel handle (e.g., '@channelhandle')."
    )
    max_results: int = Field(10, description="The maximum number of results to return.")


#  Outputs
class AddVideoToVectorDB_Output(BaseModel):
    success: bool = Field(
        ..., description="Whether the video was successfully added to the vector DB."
    )

class VideoInfo(BaseModel):
    video_id: str
    title: str
    publish_date: datetime
    video_url: str


class FetchLatestVideosFromYouTubeChannel_Output(BaseModel):
    videos: List[VideoInfo]

class ContentCreatorInfo(BaseModel):
    first_name: Optional[str] = Field(
        ..., description="The first name of the content creator"
    )
    last_name: Optional[str] = Field(
        None, description="The last name of the content creator"
    )
    main_topics_covered: Optional[List[str]] = Field(
        None, description="The main topics covered by the content creator"
    )
    bio: Optional[str] = Field(
        None, description="A brief biography of the content creator"
    )
    email_address: Optional[str] = Field(
        None, description="The email address of the content creator"
    )
    linkedin_url: Optional[str] = Field(
        None, description="The LinkedIn profile URL of the content creator"
    )
    has_linked_in: Optional[bool] = Field(
        None, description="Whether the content creator has a LinkedIn profile"
    )
    x_url: Optional[str] = Field(
        None, description="The Twitter (X) profile URL of the content creator"
    )
    has_twitter: Optional[bool] = Field(
        None, description="Whether the content creator has a Twitter (X) profile"
    )
    has_skool: Optional[bool] = Field(
        None, description="Whether the content creator has a Skool profile"
    )