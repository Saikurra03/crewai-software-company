import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app import run_crew

st.set_page_config(
    page_title="AI Software Company",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: #6C63FF;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        color: #666;
        font-size: 1.1rem;
    }
    .agent-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        border-radius: 8px;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🤖 AI Software Company</h1>
    <p>Enter your project idea and let 4 AI agents plan it for you</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="agent-card"><h4>📋</h4><p><strong>Project Manager</strong></p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="agent-card"><h4>🏗️</h4><p><strong>Architect</strong></p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="agent-card"><h4>💻</h4><p><strong>Developer</strong></p></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="agent-card"><h4>🔍</h4><p><strong>QA Engineer</strong></p></div>""", unsafe_allow_html=True)

st.divider()

project_idea = st.text_area(
    "📝 Enter Your Project Idea",
    placeholder="e.g., A mobile app for tracking daily habits and productivity...",
    height=150
)

if st.button("🚀 Start Planning", type="primary"):
    if not project_idea.strip():
        st.error("Please enter a project idea!")
    else:
        status_area = st.empty()
        progress = st.progress(0, text="Starting...")

        def update_status(msg):
            status_area.info(f"⏳ {msg}")

        try:
            progress.progress(10, text="Initializing agents...")
            result = run_crew(project_idea, status_callback=update_status)

            progress.progress(100, text="Done!")
            st.success("✅ Project Planning Complete!")
            st.divider()

            st.markdown("## 📄 Your Project Plan")
            st.markdown(result)

            st.download_button(
                label="📥 Download Plan",
                data=result,
                file_name="project_plan.md",
                mime="text/markdown"
            )

        except Exception as e:
            progress.progress(0, text="Failed")
            st.error(f"❌ **Error:** {type(e).__name__}")
            st.code(str(e))
            st.info("💡 Check your COHERE_API_KEY in .env and make sure you have internet connection.")

st.divider()
st.markdown("""<div style='text-align: center; color: #888; font-size: 0.9rem;'>Powered by CrewAI | Built with Streamlit</div>""", unsafe_allow_html=True)
