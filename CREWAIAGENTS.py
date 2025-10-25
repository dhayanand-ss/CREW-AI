from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Verify API key is loaded
if not os.getenv('OPENAI_API_KEY'):
    print("Warning: OPENAI_API_KEY not found in environment variables.")
    print("Please create a .env file with your API key or set the environment variable.")
    print("See .env.example for the required format.")
    exit(1)
else:
    print("OpenAI API key loaded successfully!")

# Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher',
    goal='Research and gather comprehensive information about the topic {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in researching AI, Data Science, Machine Learning and GEN AI topics. "
        "You have deep knowledge of these fields and can provide detailed insights and analysis."
    ),
    allow_delegation=True
)

# Create a senior blog writer agent
blog_writer = Agent(
    role='Blog Writer',
    goal='Create compelling and educational content about the topic {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner"
    ),
    allow_delegation=False
)

# Research Task
research_task = Task(
    description=(
        "Research and analyze the topic '{topic}'. "
        "Gather comprehensive information, key concepts, and important details. "
        "Focus on providing accurate and up-to-date information."
    ),
    expected_output='A comprehensive 3 paragraphs long research report based on the topic {topic}',
    agent=blog_researcher,
)

# Writing task
write_task = Task(
    description=(
        "Create engaging blog content about the topic '{topic}' based on the research. "
        "Write in a clear, accessible style that educates readers while keeping them engaged."
    ),
    expected_output='A well-structured blog post about the topic {topic} with clear explanations and examples',
    agent=blog_writer,
    async_execution=False,
    output_file='new_blog-post.md'
)

# Create the crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Execute the crew
if __name__ == "__main__":
    print("Starting CrewAI agents...")
    print("Topic: AI vs ML vs DL vs Data Science")
    print("=" * 50)
    
    result = crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data Science'})
    
    print("\n" + "=" * 50)
    print("RESULT:")
    print(result)