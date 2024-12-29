
from crewai_tools import FirecrawlSearchTool, RagTool
from crewai_tools.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
import os
from .custom_tool import AddVideoToVectorDB_Tool , FetchLatestVideosFromYouTubeChannel_Tool 

# fire_crawl_search_tool = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))
fetch_latest_videos_tool = FetchLatestVideosFromYouTubeChannel_Tool()
add_video_to_vector_db_tool = AddVideoToVectorDB_Tool()
# fire_crawl_search_tool = FirecrawlSearchTool(api_key=os.getenv('FIRECRAWL_API_KEY'))
rag_tool = RagTool(
    config=dict(
        llm=dict(
            provider='google',
            config=dict( 
                model="gemini/gemini-1.5-flash", 
                api_key=os.getenv('GOOGLE_API_KEY')
                 ),
        )
        ,
        embedder=dict(
            provider='google',
            config=dict(
                    model="models/embedding-001", 
                    task_type="retrieval_document",
                    
            )
        )
    )
)



class FirecrawlApp(BaseModel):
    api_key: str

    # Define any other necessary methods and attributes

class FirecrawlSearchTool(BaseTool):
    name: str = "Firecrawl Search Tool"
    description: str = "Search the web using Firecrawl."
    api_key: str

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_rebuild()

    def _run(self, search_query: str) -> str:
        # Implement the tool's functionality here
        pass

# Initialize the tool
fire_crawl_search_tool = FirecrawlSearchTool(api_key=os.getenv('FIRECRAWL_API_KEY'))
