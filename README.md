# 📬 Smart Email Summarizer (CrewAI + Streamlit)

A simple agentic app that reads long emails, summarizes them, and reviews the summaries — all using LLMs and CrewAI agents. It’s designed for busy people who don’t want to waste time digging through long threads.

Built with:
- 🧠 [CrewAI] to manage multi-agent collaboration
- ⚙️ [LiteLLM] for easy LLM switching (OpenAI, Claude, Gemini, etc.)
- 🖥️ [Streamlit] for a fast, clean UI

---

## 💡 Why I Made This

I noticed that people (myself included) waste a lot of time reading long or repetitive emails. Summaries help — but not if they’re low-quality. So I built this tool with two agents:

1. **Summarizer Agent** – reads the email and creates a structured summary  
2. **Reviewer Agent** – checks if the summary is clear, well-written, and covers everything important

This project also helped me explore agent-based workflows, memory, and tool usage in a real-world scenario.

---

## 🔍 What It Does

- Accepts email input 
- Summarizes the email using LLMs
- Reviews the summary for clarity and completeness
- Shows both the summary and reviewer feedback in a clean UI

---

