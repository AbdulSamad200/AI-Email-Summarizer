"""
Agents package for CrewAI email summarizer.
"""

from .summarizer_agent import SummarizerAgent
from .reviewer_agent import ReviewerAgent

__all__ = ['SummarizerAgent', 'ReviewerAgent']