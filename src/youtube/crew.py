from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# custom imports
from .tools.types import ContentCreatorInfo
from .tools.tools import (
	add_video_to_vector_db_tool,fetch_latest_videos_tool,
	rag_tool,website_search_tool
)


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Youtube():
	"""Youtube crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	
	# scrape_agent
	@agent
	def scrape_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['scrape_agent'],
			verbose=True,
			tools=[fetch_latest_videos_tool]
		)

	# vector_db_agent
	@agent
	def vector_db_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['vector_db_agent'],
			verbose=True,
			tools=[add_video_to_vector_db_tool]
		)
	
	# general_research_agent
	@agent
	def general_research_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['general_research_agent'],
			verbose=True,
			tools=[rag_tool]
		)
	
	# follow_up_agent
	@agent
	def follow_up_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['follow_up_agent'],
			verbose=True,
			tools=[rag_tool]
		)
	
	# fallback_agent
	@agent
	def fallback_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['fallback_agent'],
			verbose=True,
			tools=[website_search_tool]
			# tools=[fire_crawl_search_tool]
		)
	

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task

	
	# scrape_youtube_channel_task
	@task
	def scrape_youtube_channel_task(self) -> Task:
		return Task(
			config=self.tasks_config['scrape_youtube_channel_task'],
			tools=[fetch_latest_videos_tool],
			
		)
	
	# process_videos_task
	@task
	def process_videos_task(self) -> Task:
		return Task(
			config=self.tasks_config['process_videos_task'],
			tools=[add_video_to_vector_db_tool],
			
		)
	
	# find_initial_information_task
	@task
	def find_initial_information_task(self) -> Task:
		return Task(
			config=self.tasks_config['find_initial_information_task'],
			tools=[rag_tool],
			output_pydantic=ContentCreatorInfo
		)
	
	# follow_up_task
	@task
	def follow_up_task(self) -> Task:
		return Task(
			config=self.tasks_config['follow_up_task'],
			tools=[rag_tool],
			output_pydantic=ContentCreatorInfo
			
		)
	
	# fallback_task
	@task
	def fallback_task(self) -> Task:
		return Task(
			config=self.tasks_config['fallback_task'],
			tools=[website_search_tool],
			# tools=[fire_crawl_search_tool],
			output_pydantic=ContentCreatorInfo
			
		)
	
	


	@crew
	def crew(self) -> Crew:
		"""Creates the Youtube crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
