"""
Streamlit UI for Email Summarizer
This module provides the web interface for the email summarization tool.

STYLING UPDATES APPLIED:
- Implemented cohesive dark theme throughout the application
- Modern typography using Inter font family
- Enhanced button styling with hover effects and gradients
- Dark-themed summary, review, and metric boxes with subtle borders
- Improved text area styling to blend with dark theme
- Added subtle animations and transitions
- Professional color palette with proper contrast
- Enhanced spacing and visual hierarchy
- Modern card-based design for metrics
- Improved sidebar styling with glass-morphism effect
"""

import streamlit as st
from main import EmailSummarizerCrew
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Email Summarizer",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional dark theme
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Dark theme for main app */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Headers styling */
    h1, h2, h3 {
        color: #fafafa !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
    }
    
    /* All subheaders white */
    .stSubheader, [data-testid="stSubheader"] {
        color: #fafafa !important;
    }
    
    /* Main headers spacing */
    h2 {
        margin-top: 2.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* First header no top margin */
    h2:first-of-type {
        margin-top: 0 !important;
    }
    
    /* Refined summary box dark theme */
    .refined-summary-box {
        background: linear-gradient(135deg, #1e293b 0%, #262c3b 100%);
        padding: 24px;
        border-radius: 12px;
        margin: 16px 0;
        border: 1px solid rgba(168, 85, 247, 0.2);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        color: #e2e8f0;
        line-height: 1.6;
        transition: all 0.3s ease;
    }
    
    .refined-summary-box:hover {
        border-color: rgba(168, 85, 247, 0.4);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5);
    }
    
    /* Success message styling for dark theme */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
    }
    
    /* Error message styling for dark theme */
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
    }
    
    /* Info message styling for dark theme */
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Sidebar styling with glass effect */
    section[data-testid="stSidebar"] {
        background-color: rgba(17, 25, 40, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: #e0e0e0 !important;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background-color: #1a1f2e !important;
        color: #fafafa !important;
        border: 1px solid #2d3748 !important;
        border-radius: 8px !important;
        font-family: 'JetBrains Mono', 'Courier New', monospace !important;
        font-size: 14px !important;
        padding: 12px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #4a5568 !important;
        box-shadow: 0 0 0 1px #4a5568 !important;
    }
    
    /* Text area label styling */
    .stTextArea label {
        color: #fafafa !important;
        font-weight: 500 !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        text-transform: none !important;
        letter-spacing: 0.02em !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Primary button special styling */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%) !important;
        font-size: 1.1rem !important;
        padding: 1rem 2rem !important;
    }
    
    /* Summary box dark theme */
    .summary-box {
        background: linear-gradient(135deg, #1e293b 0%, #1a202c 100%);
        padding: 24px;
        border-radius: 12px;
        margin: 16px 0;
        border: 1px solid rgba(139, 92, 246, 0.2);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        color: #e2e8f0;
        line-height: 1.6;
        transition: all 0.3s ease;
    }
    
    .summary-box:hover {
        border-color: rgba(139, 92, 246, 0.4);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5);
    }
    
    /* Review box dark theme */
    .review-box {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        padding: 24px;
        border-radius: 12px;
        margin: 16px 0;
        border: 1px solid rgba(34, 197, 94, 0.2);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        color: #e2e8f0;
        line-height: 1.6;
        transition: all 0.3s ease;
    }
    
    .review-box:hover {
        border-color: rgba(34, 197, 94, 0.4);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5);
    }
    
    /* Metric card dark theme */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 12px 0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.4);
    }
    
    [data-testid="metric-container"] label {
        color: #e2e8f0 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #f1f5f9 !important;
        font-weight: 600 !important;
        font-size: 1.75rem !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #1e293b !important;
        border-radius: 8px !important;
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #334155 !important;
    }
    
    /* Success/Error message styling */
    .stAlert > div {
        border-radius: 8px !important;
        border: 1px solid !important;
        padding: 16px !important;
    }
    
    /* Success alert specific dark theme styling */
    .stAlert[data-baseweb="notification"] > div {
        background-color: #1a2e1a !important;
        color: #e2e8f0 !important;
        border-color: rgba(34, 197, 94, 0.3) !important;
    }
    
    .stAlert[data-baseweb="notification"] svg {
        fill: #22c55e !important;
    }
    
    div[data-baseweb="notification"] {
        border-radius: 8px !important;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-color: #667eea !important;
        border-right-color: transparent !important;
    }
    
    /* Divider styling */
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, #4a5568, transparent) !important;
        margin: 2rem 0 !important;
    }
    
    /* Footer styling */
    .footer-text {
        text-align: center;
        color: #94a3b8;
        margin-top: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.5) 100%);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .footer-text p {
        margin: 0.5rem 0;
        font-size: 0.875rem;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a202c;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #4a5568;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #718096;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'crew' not in st.session_state:
    st.session_state.crew = EmailSummarizerCrew()
if 'processing_history' not in st.session_state:
    st.session_state.processing_history = []

# Header
st.title("🤖 AI Email Summarizer with CrewAI")
st.markdown("**Built with CrewAI agents, LiteLLM, and Gemini Pro**")

# Sidebar
with st.sidebar:
    st.header("📋 About This App")
    st.markdown("""
    This application demonstrates:
    - **CrewAI** agent orchestration
    - **LiteLLM** for LLM routing
    - **Gemini Pro** for AI processing
    - **Streamlit** for UI
    
    ### How it works:
    1. Paste your email
    2. AI agents summarize it
    3. Quality review provided
    4. Optional refinement available
    """)
    
    # API Key status
    st.header("🔑 API Status")
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        st.success("✅ Gemini API Key Configured")
    else:
        st.error("❌ Gemini API Key Missing")
        st.info("Add GEMINI_API_KEY to your .env file")
    
    # Sample email loader
    st.header("📝 Load Sample Email")
    if st.button("Load Example Email"):
        st.session_state.email_input = """Subject: Q4 Planning Meeting - Action Required

Hi Team,

I hope this email finds you well. I wanted to follow up on our discussion from last week's leadership meeting and outline the next steps for our Q4 planning.

First, I need everyone to submit their departmental goals by October 15th. Please use the new template that Sarah shared last Tuesday. Make sure to include both stretch goals and minimum viable targets.

Second, we've decided to move forward with the new product launch in November. Marketing needs to have the campaign ready by November 1st, and Engineering must complete the final testing phase by October 25th. This is a hard deadline as we've already committed to our partners.

Third, regarding the budget discussions, finance will be sending out the revised allocations by end of day tomorrow. Please review them carefully and flag any concerns by October 10th. We need to finalize everything before the board meeting on October 20th.

I've also attached the meeting notes from yesterday's strategy session. There are some important changes to our customer success approach that everyone should be aware of.

Lastly, don't forget about the team building event on October 18th. HR needs final headcount by October 8th.

Let me know if you have any questions. This is going to be a busy month, but I'm confident we can deliver on all fronts.

Best regards,
John"""

# Main content area - Email Input Section
st.header("📧 Email Input")
email_input = st.text_area(
    "Paste your email here:",
    value=st.session_state.get('email_input', ''),
    height=400,
    placeholder="Paste a long email here to see the AI agents in action..."
)

# Process button
process_button = st.button("🚀 Summarize Email", type="primary", use_container_width=True)

# Process email when button is clicked
if process_button and email_input:
    with st.spinner("🤖 CrewAI agents are analyzing your email..."):
        # Process the email
        result = st.session_state.crew.process_email(email_input)
        
        # Store in session state
        st.session_state.last_result = result
        st.session_state.last_email = email_input
        
        # Add to history
        st.session_state.processing_history.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'email_preview': email_input[:100] + "...",
            'result': result
        })

# Display results - AI Analysis Results Section
if 'last_result' in st.session_state:
    result = st.session_state.last_result
    
    # AI Analysis Results
    st.header("📊 AI Analysis Results")
    
    # Summary section
    st.subheader("📝 Summary")
    with st.container():
        st.markdown(f'<div class="summary-box">{result["summary"]}</div>', unsafe_allow_html=True)
    
    # Quality Review as separate main section
    st.header("🔍 Quality Review")
    with st.container():
        st.markdown(f'<div class="review-box">{result["review"]}</div>', unsafe_allow_html=True)
    
    # Refinement option
    if st.button("🔄 Refine Summary", use_container_width=True):
        with st.spinner("Refining summary based on feedback..."):
            refined_summary = st.session_state.crew.refine_summary(
                st.session_state.last_email,
                result["summary"],
                result["review"]
            )
            st.subheader("✨ Refined Summary")
            st.markdown(f'<div class="refined-summary-box">{refined_summary}</div>', unsafe_allow_html=True)

# Metrics section - Processing Metrics
if 'processing_history' in st.session_state and st.session_state.processing_history:
    st.header("📈 Processing Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Emails Processed", len(st.session_state.processing_history))
    
    with col2:
        success_count = sum(1 for h in st.session_state.processing_history if h['result']['status'] == 'success')
        st.metric("Successful Summaries", success_count)
    
    with col3:
        if st.session_state.processing_history:
            st.metric("Last Processed", st.session_state.processing_history[-1]['timestamp'])

# History expander
with st.expander("📜 Processing History"):
    for i, hist in enumerate(reversed(st.session_state.processing_history[-5:])):  # Show last 5
        st.write(f"**{hist['timestamp']}** - {hist['email_preview']}")
        if st.button(f"View Details", key=f"hist_{i}"):
            st.write("Summary:", hist['result']['summary'])
            st.write("Review:", hist['result']['review'])

# Footer
st.markdown("---")
st.markdown("""
<div class='footer-text'>
    <p>Built with ❤️ using CrewAI, LiteLLM, and Streamlit</p>
    <p>Ready for deployment on Streamlit Cloud 🚀</p>
</div>
""", unsafe_allow_html=True)