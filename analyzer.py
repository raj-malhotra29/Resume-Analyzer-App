import google.generativeai as genai

# Apni API Key yahan dalein
genai.configure(api_key="AIzaSyCryyR7CuSZ37yfdvVJD9vtSqkjJ9qPObk")

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
    