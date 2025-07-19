"""
Feedback Tool
This tool provides quality assessment and feedback on email summaries.
"""

from crewai.tools import BaseTool
from litellm import completion
import os
from typing import Dict, Any


class FeedbackTool(BaseTool):
    name: str = "Summary Feedback Analyzer"
    description: str = "Analyzes email summaries and provides quality feedback"
    
    def _run(self, original_email: str, summary: str) -> str:
        """
        Analyze a summary and provide feedback.
        
        Args:
            original_email: The original email text
            summary: The summary to review
            
        Returns:
            Detailed feedback on the summary quality
        """
        try:
            # Check if API key is available
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return self._get_fallback_feedback()
            
            # Prepare the review prompt
            prompt = f"""You are an expert editor reviewing an email summary. 

ORIGINAL EMAIL:
{original_email}

SUMMARY TO REVIEW:
{summary}

Please provide a detailed review including:

1. QUALITY SCORE: (1-10, where 10 is perfect)
2. ACCURACY CHECK: Does the summary accurately represent the email?
3. COMPLETENESS: Are all key points covered?
4. CLARITY: Is the summary clear and well-structured?
5. STRENGTHS: What does the summary do well?
6. IMPROVEMENTS: What could be better?
7. SUGGESTED REVISIONS: Specific changes to improve the summary

Be constructive and specific in your feedback."""

            # Use LiteLLM with Gemini
            response = completion(
                model="gemini/gemini-pro",
                messages=[{"role": "user", "content": prompt}],
                api_key=api_key,
                temperature=0.4,
                max_tokens=600
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error in feedback generation: {str(e)}")
            return self._get_fallback_feedback()
    
    def _get_fallback_feedback(self) -> str:
        """
        Provide basic feedback when API is unavailable.
        
        Returns:
            Basic feedback message
        """
        return """**FALLBACK FEEDBACK (API Key Missing)**

QUALITY SCORE: N/A

FEEDBACK:
• Unable to provide AI-powered feedback without API access
• Please configure your GEMINI_API_KEY in the .env file
• Once configured, you'll receive detailed quality assessments

SUGGESTED ACTION:
1. Create a .env file based on .env.example
2. Add your Gemini API key
3. Restart the application

Note: AI-powered review features require a valid Gemini API key."""