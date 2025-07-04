
---

**📰 Gemini News Summarizer & Chatbot**

An AI-powered web application that summarizes news and answers your queries in both English and हिंदी. It supports voice playback, PDF export, WhatsApp sharing, and is fully responsive with dark mode.

**🔗 Live App**
[https://news-summarizer-u9kv.onrender.com](https://news-summarizer-u9kv.onrender.com)

---

**Key Features**

• Summarize India & World news
• Language support: English / हिंदी
• Text-to-speech for summary
• Share on WhatsApp
• Download summary as PDF
• AI chatbot for news-related questions
• Fully responsive UI with dark mode

---

**How to Run Locally**

1. Clone the repository
   `git clone https://github.com/sanyagupta31/news_summarizer.git`

2. Navigate into the project
   `cd news_summarizer`

3. Create a virtual environment
   `python -m venv venv`
   Activate it:
   `venv\Scripts\activate` (Windows)
   `source venv/bin/activate` (macOS/Linux)

4. Install dependencies
   `pip install -r requirements.txt`

5. Create a `.env` file and add your Gemini API key

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

6. Run the app
   `python app.py`
   Open in browser: `http://localhost:5000`

---

**Deploying on Render**

• Set up a new **Web Service** on [Render](https://render.com)
• Choose your GitHub repo
• Set build command to: *(leave empty)*
• Set start command to:
`python app.py`

• Add environment variable:
`GOOGLE_API_KEY = your_api_key_here`

---

**Technologies Used**

• Python & Flask
• HTML, CSS, JavaScript
• Google Gemini API
• Render for deployment

---

**Author**

Created by Sanya Gupta
GitHub: [sanyagupta31](https://github.com/sanyagupta31)

---

