
from crewai_tools.tools.base_tool import BaseTool
from crewai_tools import YoutubeVideoSearchTool
from dotenv import load_dotenv
from embedchain import App
from embedchain.models.data_type import DataType
from pydantic.v1 import BaseModel, Field
from typing import Type,List
import requests
from datetime import datetime, timezone
import os

from datetime import datetime, timezone
from .types import (AddVideoToVectorDB_Input,AddVideoToVectorDB_Output,FetchLatestVideosFromYouTubeChannel_Input,
                    FetchLatestVideosFromYouTubeChannel_Output,VideoInfo
)


class AddVideoToVectorDB_Tool(BaseTool):
   
    name: str = "Add Video to Vector DB"
    description: str = "Adds a YouTube video to the vector database."
    # args_schema: Type[BaseModel] = AddVideoToVectorDB_Input
    return_schema: Type[BaseModel] = AddVideoToVectorDB_Output

    def _run(self, video_url: str) -> AddVideoToVectorDB_Output:
        try:
            os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')  
            tool = YoutubeVideoSearchTool(
            config=dict(
                # llm=dict(
                #     provider="ollama", # or google, openai, anthropic, llama2, ...
                #     config=dict(
                #         model="llama2",
                #         # temperature=0.5,
                #         # top_p=1,
                #         # stream=true,
                #     ),
                # ),
                embedder=dict(
                    provider="google", # or openai, ollama, ...
                    config=dict(
                        model="models/embedding-001",
                        task_type="retrieval_document",
                        # title="Embeddings",
                    ),
                 ),
                )
            )
        
            # app = App.from_config(config_path='config.yaml')
            # app.add(video_url, data_type=DataType.YOUTUBE_VIDEO)
            return AddVideoToVectorDB_Output(success=True)
        except Exception as e:
            print(f'AddVideoToVectorDB_Tool failed error: {e}')
            return AddVideoToVectorDB_Output(success=False)







class FetchLatestVideosFromYouTubeChannel_Tool(BaseTool):
    name: str = "Fetch Latest Videos for Channel"
    description: str = (
        "Fetches the latest videos for a specified YouTube channel handle."
    )
    # args_schema: Type[BaseModel] = FetchLatestVideosFromYouTubeChannel_Input
    return_schema: Type[BaseModel] = FetchLatestVideosFromYouTubeChannel_Output

    def _run(
        self,
        youtube_channel_handle: str,
        max_results: int = 10,
    ) -> FetchLatestVideosFromYouTubeChannel_Output:
        api_key = os.getenv("YOUTUBE_API_KEY")

        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "type": "channel",
            "q": youtube_channel_handle,
            "key": api_key,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        items = response.json().get("items", [])
        if not items:
            raise ValueError(f"No channel found for handle {youtube_channel_handle}")

        channel_id = items[0]["id"]["channelId"]

        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "channelId": channel_id,
            "maxResults": max_results,
            "order": "date",
            "type": "video",
            "key": api_key,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        items = response.json().get("items", [])

        videos = []
        for item in items:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            publish_date = datetime.fromisoformat(
                item["snippet"]["publishedAt"].replace("Z", "+00:00")
            ).astimezone(timezone.utc)
            videos.append(
                VideoInfo(
                    video_id=video_id,
                    title=title,
                    publish_date=publish_date,
                    video_url=f"https://www.youtube.com/watch?v={video_id}",
                )
            )

        
        return FetchLatestVideosFromYouTubeChannel_Output(videos=videos)
