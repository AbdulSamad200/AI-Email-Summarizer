"""
Reviewer Agent Module
This module defines the summary reviewer agent using CrewAI framework.
"""

from crewai import Agent
from tools.feedback_tool import FeedbackTool


class ReviewerAgent:
    """Agent responsible for reviewing and providing feedback on email summaries."""
    
    def __init__(self):
        self.tool = FeedbackTool()
    
    def create_agent(self):
        """Create and return the reviewer agent."""
        return Agent(
            role="Quality Assurance Editor",
            goal="Review email summaries for accuracy, completeness, and clarity, providing constructive feedback to ensure the highest quality of communication",
            backstory="""You are a meticulous editor with a background in both technical writing 
            and business communication. You've spent 10 years as the chief editor for a major 
            business publication, where you developed a keen eye for clarity, accuracy, and 
            completeness. You believe that a good summary should be so clear that someone 
            who hasn't read the original email can make informed decisions based solely on 
            the summary. You're known for your constructive feedback that helps improve 
            communication without being overly critical.""",
            tools=[self.tool],
            verbose=True,
            allow_delegation=False,
            max_iter=2
        )
    
    def get_review_prompt(self):
        """Return the prompt template for summary review."""
        return """Please review the following email summary for quality and effectiveness:

ORIGINAL EMAIL:
{original_email}

SUMMARY PROVIDED:
{summary}

Please evaluate the summary based on:
1. **Accuracy**: Does the summary accurately reflect the email content?
2. **Completeness**: Are all important points captured?
3. **Clarity**: Is the summary easy to understand?
4. **Actionability**: Are action items clearly identified?
5. **Conciseness**: Is the summary appropriately brief while maintaining completeness?

Provide:
- A quality score (1-10)
- Specific strengths of the summary
- Areas for improvement
- Suggested revisions (if any)

Be constructive and specific in your feedback."""