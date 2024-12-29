# Youtube Crew

Welcome to the Youtube Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**
**Set up environment variables**:
Create a `.env` file in the root directory and in relevant subdirectories (1_pdf, 2_youtube_and_web) with your API keys and other configurations.

```env
MODEL=gemini/gemini-1.5-flash
GOOGLE_API_KEY=
GEMINI_API_KEY=
YOUTUBE_API_KEY=
FIRECRAWL_API_KEY=
# Add other necessary environment variables
```

- Modify `src/youtube/config/agents.yaml` to define your agents
- Modify `src/youtube/config/tasks.yaml` to define your tasks
- Modify `src/youtube/crew.py` to add your own logic, tools and specific args
- Modify `src/youtube/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the youtube Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The youtube Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

### YouTube Processing Agents and Tasks

#### Agents

1. **Scrape Agent**: Extracts content from YouTube videos and adds it to the vector database.
2. **Vector DB Processor**: Adds YouTube videos to the vector database.
3. **General Research Agent**: Gathers all required information from the YouTube channel.
4. **Follow-up Agent**: Performs thorough research to find any missing data.
5. **Fallback Agent**: Conducts final checks and searches the internet for any remaining information.

#### Tasks

1. **Scrape YouTube Channel Task**: Extracts information from the latest five videos of a specified YouTube channel.
2. **Process Videos Task**: Adds the extracted video URLs to the vector database.
3. **Find Initial Information Task**: Fills out the `ContentCreatorInfo` model with as much information as possible.
4. **Follow-up Task**: Searches for any missing data in the `ContentCreatorInfo` model.
5. **Fallback Task**: Performs final checks to ensure the `ContentCreatorInfo` model is fully populated.

## YouTube API Setup

To use the YouTube Data API v3 for this project, follow these steps:

1. **Enable the YouTube Data API v3**:

   - Go to the [YouTube Data API v3 page](https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search&project=crewai-415713) on Google Cloud Console.
   - Click on **Enable**.

2. **Create API Credentials**:
   - Go to the [API Credentials page](https://console.cloud.google.com/apis/credentials?project=crewai-415713) on Google Cloud Console.
   - Click on **Create Credentials** and select **API Key**.
   - Copy the generated API key and add it to your `.env` file as `YOUTUBE_API_KEY`.

## Goal

The primary goal of this project is to help people get comfortable with using RAG (Retrieval-Augmented Generation) techniques. This includes:

- **Scraping**: Extracting content from various sources.
- **Embedding**: Adding content to a vector database.
- **Querying**: Searching for information within the vector database.
- **Making and Using Tools**: Creating custom tools and using existing tools effectively.

### Use Cases

1. **Searching for Information in a Vector Store**: If the information is not found, look elsewhere.
   - Example: Hiring a job candidate and searching their resume.
   - Example: Sales job needing information about potential customers.
   - Example: Company looking through internal docs to answer a question before falling back to the web.

## Contributing

We welcome contributions to enhance the functionality and features of this project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For support, questions, or feedback regarding the Youtube Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
