import google.generativeai as genai
import streamlit as st
# Apni API Key yahan dalein
api_key = st.secrets["GOOGLE_API_KEY"] 
genai.configure(api_key=api_key)
def analyze_resume(resume_text):
    """
    Resume text ko analyze karke skills, experience, aur suggestions return karta hai.
    """
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    Aap ek professional career coach hain. Niche diye gaye resume ko analyze karein aur JSON format mein result dein:
    1. Skills (List)
    2. Years of Experience
    3. Education
    4. 3-5 actionable suggestions to improve this resume.

    Resume Text:
    {resume_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in Analysis: {e}"
    