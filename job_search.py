import pandas as pd

def find_jobs(skills):
    # Agar search nahi chal raha, toh direct portals return karein
    default_jobs = [
        {"title": "Junior Python Developer", "company": "Naukri", "location": "India", "link": "https://www.naukri.com/python-jobs"},
        {"title": "Web Development Internship", "company": "Indeed", "location": "India", "link": "https://in.indeed.com/jobs?q=web+developer+intern"},
        {"title": "Software Developer Trainee", "company": "LinkedIn", "location": "India", "link": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer"},
        {"title": "BCA Graduate Jobs", "company": "Glassdoor", "location": "India", "link": "https://www.glassdoor.co.in/Job/india-bca-jobs-SRCH_IL.0,5_IN115_KO6,9.htm"}
    ]
    return pd.DataFrame(default_jobs)