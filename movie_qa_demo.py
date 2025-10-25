"""
Movie Q&A Agent Demo
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get workflow ID from environment variable
WORKFLOW_ID = os.getenv('AGENTKIT_WORKFLOW_ID', 'your-workflow-id-here')

def ask_movie_question(question):
    """Ask a movie question to the agent with web search"""
    print(f"🎬 Question: {question}")
    print("🔍 Searching the web for movie information...")
    
    # Simulate API call to your AgentKit workflow with web search
    try:
        # This would be your actual API call to the workflow
        # response = call_agentkit_workflow(WORKFLOW_ID, question)
        
        # For demo purposes, simulate web search response
        print("✅ Answer: [Web search results would appear here]")
        print("   Your AgentKit workflow with web search is processing the question...")
        print("   This would return real-time movie information from the web.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("✅ Answer: I'm a movie Q&A agent with web search! Ask me about any movie, director, or actor.")

def main():
    print("🎬 MOVIE Q&A AGENT DEMO")
    print(f"Workflow ID: {WORKFLOW_ID}")
    print("=" * 40)
    
    # Sample questions
    questions = [
        "What is Inception about?",
        "Who directed The Matrix?", 
        "Tell me about Titanic"
    ]
    
    for q in questions:
        ask_movie_question(q)
        print()
    
    # Interactive mode
    print("Ask your own questions (type 'quit' to exit):")
    while True:
        question = input("🎬 Your question: ").strip()
        if question.lower() == 'quit':
            break
        if question:
            ask_movie_question(question)
            print()

if __name__ == "__main__":
    main()
