
from crewai_tools import SerperDevTool, RagTool
from pydantic import Field
from .custom_tool import AddVideoToVectorDB_Tool , FetchLatestVideosFromYouTubeChannel_Tool 
import os


fetch_latest_videos_tool = FetchLatestVideosFromYouTubeChannel_Tool()
add_video_to_vector_db_tool = AddVideoToVectorDB_Tool()
website_search_tool = SerperDevTool()



# rag_tool = RagTool(
#     config=dict(
#         llm=dict(
#             provider='google',
#             config=dict( 
#                 model="gemini/gemini-1.5-flash", 
#                 api_key=os.getenv('GOOGLE_API_KEY')
#                  ),
#         )
#         ,
#         embedder=dict(
#             provider='google',
#             config=dict(
#                     model="models/embedding-001", 
#                     task_type="retrieval_document",
                    
#             )
#         )
#     )
# )

rag_tool = RagTool(
    config={
        "llm": {
            "provider": "google",
            "config": {
                "model": "gemini-1.5-flash",  # Specify the desired Google LLM
            },
        },
        "embedding_model": {
            "provider": "google",
            "config": {
                "model": "models/text-embedding-004",  # Specify the desired Google embedding model
            },
        },
    }
)