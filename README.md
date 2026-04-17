# CREW-AI

Multi-agent AI workflows built with CrewAI, demonstrating automated blog content generation and a movie Q&A agent.

## Overview

This project showcases the CrewAI framework for orchestrating AI agents:

- **Blog Generation Crew** -- A researcher agent gathers information on a given topic, then a writer agent produces a polished blog post.
- **Movie Q&A Demo** -- An interactive agent that answers movie-related questions using web search.

## Tech Stack

- Python 3.10+
- [CrewAI](https://github.com/joaomdmoura/crewAI) (multi-agent orchestration)
- OpenAI API (LLM backend)
- python-dotenv (environment management)

## Setup

```bash
git clone https://github.com/dhayanand-ss/CREW-AI.git
cd CREW-AI
pip install crewai crewai-tools python-dotenv
cp .env.example .env
# Add your OPENAI_API_KEY to .env
```

## Usage

```bash
# Run the blog generation crew
python CREWAIAGENTS.py

# Run the movie Q&A demo
python movie_qa_demo.py
```

## Project Structure

| File | Description |
|------|-------------|
| `CREWAIAGENTS.py` | Main CrewAI blog researcher + writer pipeline |
| `movie_qa_demo.py` | Movie Q&A agent with web search |
| `INSTALLATION_GUIDE.md` | Detailed setup instructions |
| `.env.example` | Environment variable template |
