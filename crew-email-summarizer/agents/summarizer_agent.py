"""
Summarizer Agent Module
This module defines the email summarizer agent using CrewAI framework.
"""

from crewai import Agent
from tools.summarizer_tool import EmailSummarizerTool


class SummarizerAgent:
    """Agent responsible for summarizing long emails into concise, actionable summaries."""
    
    def __init__(self):
        self.tool = EmailSummarizerTool()
    
    def create_agent(self):
        """Create and return the summarizer agent."""
        return Agent(
            role="Senior Email Communication Specialist",
            goal="Extract the most important information from emails and create clear, concise summaries that highlight key points, action items, and decisions",
            backstory="""You are an experienced executive assistant with over 15 years of experience 
            working with C-level executives. You have developed an exceptional ability to quickly 
            read through lengthy emails and extract the essence of the communication. Your summaries 
            have helped busy professionals save hours of reading time while never missing critical 
            information. You are known for your ability to identify hidden action items and 
            implicit requests that others might miss.""",
            tools=[self.tool],
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )
    
    def get_summarization_prompt(self):
        """Return the prompt template for email summarization."""
        return """Please analyze the following email and provide a comprehensive summary:

EMAIL CONTENT:
{email_content}

Your summary should include:
1. **Main Topic**: What is the email primarily about?
2. **Key Points**: List the 3-5 most important points
3. **Action Items**: Any tasks or actions required (with deadlines if mentioned)
4. **Decisions Needed**: Any decisions that need to be made
5. **Important Dates**: Any dates or deadlines mentioned
6. **Tone/Urgency**: The overall tone and urgency level

Format the summary in a clear, structured way that can be quickly scanned."""