"""
Main CrewAI Orchestration Module
This module handles the coordination between the summarizer and reviewer agents.
"""

from crewai import Crew, Task, Process
from agents.summarizer_agent import SummarizerAgent
from agents.reviewer_agent import ReviewerAgent
from dotenv import load_dotenv
import os
from typing import Dict, Any, Optional


# Load environment variables
load_dotenv()


class EmailSummarizerCrew:
    """Orchestrates the email summarization and review process using CrewAI."""
    
    def __init__(self):
        # Initialize agents
        self.summarizer = SummarizerAgent()
        self.reviewer = ReviewerAgent()
        
        # Create agent instances
        self.summarizer_agent = self.summarizer.create_agent()
        self.reviewer_agent = self.reviewer.create_agent()
    
    def process_email(self, email_content: str) -> Dict[str, Any]:
        """
        Process an email through summarization and review.
        
        Args:
            email_content: The email text to process
            
        Returns:
            Dictionary containing summary and review results
        """
        try:
            # Task 1: Summarize the email
            summarization_task = Task(
                description=f"""Analyze and summarize the following email. 
                Create a clear, structured summary that captures all important information.
                
                Email to summarize:
                {email_content}""",
                agent=self.summarizer_agent,
                expected_output="A structured email summary with main topics, key points, action items, and other relevant information"
            )
            
            # Task 2: Review the summary
            review_task = Task(
                description=f"""Review the email summary for quality, accuracy, and completeness.
                Provide constructive feedback and suggestions for improvement.
                
                Original email:
                {email_content}
                
                The summary will be provided by the previous task.""",
                agent=self.reviewer_agent,
                expected_output="A detailed review with quality score, strengths, areas for improvement, and specific suggestions",
                context=[summarization_task]  # This task depends on the summarization task
            )
            
            # Create and run the crew
            crew = Crew(
                agents=[self.summarizer_agent, self.reviewer_agent],
                tasks=[summarization_task, review_task],
                process=Process.sequential,  # Tasks run in order
                verbose=True
            )
            
            # Execute the crew
            result = crew.kickoff()
            
            # Parse results
            if isinstance(result, dict):
                return {
                    "summary": result.get("task_outputs", {}).get(0, "No summary generated"),
                    "review": result.get("task_outputs", {}).get(1, "No review generated"),
                    "status": "success"
                }
            else:
                # Handle string or other return types
                outputs = str(result).split("\n\n---\n\n")
                return {
                    "summary": outputs[0] if len(outputs) > 0 else str(result),
                    "review": outputs[1] if len(outputs) > 1 else "Review pending...",
                    "status": "success"
                }
                
        except Exception as e:
            return {
                "summary": f"Error processing email: {str(e)}",
                "review": "Unable to review due to processing error",
                "status": "error",
                "error": str(e)
            }
    
    def refine_summary(self, email_content: str, initial_summary: str, feedback: str) -> str:
        """
        Refine a summary based on feedback (optional multi-turn refinement).
        
        Args:
            email_content: Original email
            initial_summary: The first summary attempt
            feedback: Review feedback
            
        Returns:
            Refined summary
        """
        refinement_task = Task(
            description=f"""Based on the feedback provided, create an improved summary of the email.
            
            Original email:
            {email_content}
            
            Initial summary:
            {initial_summary}
            
            Feedback received:
            {feedback}
            
            Create a revised summary that addresses all the feedback points.""",
            agent=self.summarizer_agent,
            expected_output="An improved email summary that incorporates all feedback"
        )
        
        # Single agent crew for refinement
        crew = Crew(
            agents=[self.summarizer_agent],
            tasks=[refinement_task],
            process=Process.sequential,
            verbose=False
        )
        
        result = crew.kickoff()
        return str(result)


# Convenience function for testing
def test_crew():
    """Test the crew with a sample email."""
    sample_email = """Subject: Q4 Planning Meeting - Action Required

Hi Team,

I hope this email finds you well. I wanted to follow up on our discussion from last week's leadership meeting and outline the next steps for our Q4 planning.

First, I need everyone to submit their departmental goals by October 15th. Please use the new template that Sarah shared last Tuesday. Make sure to include both stretch goals and minimum viable targets.

Second, we've decided to move forward with the new product launch in November. Marketing needs to have the campaign ready by November 1st, and Engineering must complete the final testing phase by October 25th. This is a hard deadline as we've already committed to our partners.

Third, regarding the budget discussions, finance will be sending out the revised allocations by end of day tomorrow. Please review them carefully and flag any concerns by October 10th. We need to finalize everything before the board meeting on October 20th.

I've also attached the meeting notes from yesterday's strategy session. There are some important changes to our customer success approach that everyone should be aware of.

Lastly, don't forget about the team building event on October 18th. HR needs final headcount by October 8th.

Let me know if you have any questions. This is going to be a busy month, but I'm confident we can deliver on all fronts.

Best regards,
John
"""
    
    crew = EmailSummarizerCrew()
    result = crew.process_email(sample_email)
    
    print("=== SUMMARY ===")
    print(result["summary"])
    print("\n=== REVIEW ===")
    print(result["review"])


if __name__ == "__main__":
    test_crew()