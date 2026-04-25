import streamlit as st
from parser import extract_text_from_pdf
from analyzer import analyze_resume
from job_search import find_jobs

# Page Configuration
st.set_page_config(page_title="AI Resume Pro", layout="wide")

# Sidebar for Uploads
with st.sidebar:
    st.header("⚙️ Settings")
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    analyze_btn = st.button("Analyze Resume")

st.title("📄 AI Resume Analyzer & Job Finder")

if uploaded_file:
    # Logic to process and analyze
    if analyze_btn:
        with st.spinner("Analyzing your profile..."):
            # 1. Parse & Analyze
            text = extract_text_from_pdf(uploaded_file)
            analysis_result = analyze_resume(text)
            
            # Save results in session state so it doesn't disappear on click
            st.session_state['analysis'] = analysis_result
            st.session_state['text'] = text

    # Check if analysis exists in session state
    if 'analysis' in st.session_state:
        # Layout for Metrics
        col1, col2 = st.columns(2)
        col1.metric("Analysis Status", "Completed")
        col2.metric("Persona", "Junior Developer")
        
        # Analysis Display
        st.subheader("💡 AI Career Insights")
        st.markdown(st.session_state['analysis'])

        # Job Search Section
        st.divider()
        st.subheader("🚀 Recommended Job Openings")
        
        if st.button("Find Matching Jobs"):
            with st.spinner("Fetching opportunities..."):
                # Job Search
                jobs = find_jobs(["Python", "Java", "Web Development"])
                # DEBUGGING: Print karein ki jobs mili ya nahi
                st.write(f"DEBUG: Found {len(jobs)} jobs.")
                
                if not jobs.empty:
                    # Job Card Layout
                    cols = st.columns(2)
                    for index, row in jobs.iterrows():
                        with cols[index % 2]:
                            with st.container(border=True):
                                st.markdown(f"#### {row['title']}")
                                st.caption(f"🏢 {row['company']} | 📍 {row['location']}")
                                with st.expander("View Details"):
                                    st.write(row.get('description', 'No description available.'))
                                st.link_button("Apply Now", row['link'])
                else:
                    st.warning("No jobs found. Try adjusting keywords.")
else:
    st.info("👈 Please upload a PDF resume in the sidebar to get started!")