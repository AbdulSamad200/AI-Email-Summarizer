"""
Email Summarizer Tool
This tool handles the actual summarization logic using LiteLLM.
"""

from crewai.tools import BaseTool
from litellm import completion
import os
from typing import Dict, Any


class EmailSummarizerTool(BaseTool):
    name: str = "Email Summarizer"
    description: str = "Summarizes long emails into concise, actionable formats"
    
    def _run(self, email_content: str) -> str:
        """
        Execute the email summarization.
        
        Args:
            email_content: The full email text to summarize
            
        Returns:
            A structured summary of the email
        """
        try:
            # Check if API key is available
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return self._get_fallback_summary(email_content)
            
            # Prepare the summarization prompt
            prompt = f"""You are an expert email summarizer. Please analyze the following email and provide a structured summary.

EMAIL CONTENT:
{email_content}

Provide a summary with these sections:
1. MAIN TOPIC: (one line)
2. KEY POINTS: (bullet points)
3. ACTION ITEMS: (if any, with deadlines)
4. DECISIONS NEEDED: (if any)
5. IMPORTANT DATES: (if any)
6. TONE/URGENCY: (brief assessment)

Keep the summary concise but comprehensive."""

            # Use LiteLLM with Gemini
            response = completion(
                model="gemini/gemini-pro",
                messages=[{"role": "user", "content": prompt}],
                api_key=api_key,
                temperature=0.3,
                max_tokens=500
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error in summarization: {str(e)}")
            return self._get_fallback_summary(email_content)
    
    def _get_fallback_summary(self, email_content: str) -> str:
        """
        Provide a basic summary when API is unavailable.
        
        Args:
            email_content: The email text
            
        Returns:
            A basic summary
        """
        # Simple fallback logic
        lines = email_content.strip().split('\n')
        word_count = len(email_content.split())
        
        return f"""**FALLBACK SUMMARY (API Key Missing)**

MAIN TOPIC: Email regarding various matters

KEY POINTS:
• Email contains {word_count} words
• {len(lines)} lines of text
• Unable to process with AI - please configure GEMINI_API_KEY

ACTION ITEMS:
• Configure your Gemini API key in .env file
• Restart the application

TONE/URGENCY: Unable to assess without API access

Note: This is a fallback summary. For AI-powered summaries, please add your Gemini API key."""