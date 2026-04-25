# Resume-Analyzer-App
# 🚀 AI-Powered Resume Analyzer & Job Finder

Yeh project ek **Full-Stack Web Application** hai jo user ke PDF resume ko analyze karta hai, Gemini AI ka use karke skill gaps batata hai, aur un skills ke basis par live job openings search karta hai.

---

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **AI Engine:** Google Gemini Pro (via `google-generativeai`)
* **PDF Processing:** PyMuPDF (`fitz`)
* **Data Handling:** Pandas
* **Search:** `googlesearch-python`

---

## ⚙️ Project Working
1. **Resume Parsing:** App user ki PDF file ko read karta hai aur text extract karta hai.
2. **AI Analysis:** Extract kiya gaya text Google Gemini AI ko bheja jata hai, jo resume ko analyze karke:
   * Strengths aur Weaknesses batata hai.
   * Improvement ke liye suggestions deta hai.
   * Relevant skills identify karta hai.
3. **Smart Job Search:** AI dwara identify kiye gaye skills ke basis par, app automatic Google search karke best job openings ke links fetch karti hai.

---

## 🚀 How to Use
1. **Upload Resume:** Dashboard par "Upload your resume (PDF)" section mein apni file upload karein.
2. **Analyze:** "Analyze Resume" button par click karein. AI aapke resume ka detailed report generate karega.
3. **Find Jobs:** "Find Matching Jobs" button par click karein. Aapko apne profile se match karte huye top job links dikh jayenge.

---

## 📦 Installation & Setup (Local Environment)
Agar aap is project ko apne computer par run karna chahte hain:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Resume-Analyzer-App.git
   cd Resume-Analyzer-App
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key:**
   Apni `GOOGLE_API_KEY` ko environment variables mein set karein ya `streamlit secrets` ka use karein.

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Development Details
* **Parser Logic:** `parser.py` file mein `fitz` library ka use karke PDF ko text mein convert kiya gaya hai.
* **Analysis Logic:** `analyzer.py` mein Gemini API ke through prompt engineering ka use karke output generate kiya gaya hai.
* **Scraper Logic:** `job_search.py` mein `googlesearch` library ka use karke dynamic job links fetch kiye jaate hain.

---

## 🤝 Contributing
Agar aap is project mein naye features add karna chahte hain (jaise job description match scores), toh pull request bhej sakte hain!

---
*Created with ❤️ by [Your Name]*
 project open karke samajh sakega ki yeh kaise kaam karta hai. 

PROJECT WORKING LINK :- https://mb22bkzi2rpemdhnhcx5fy.streamlit.app/
