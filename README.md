

📰 Gemini News Summarizer

Gemini News Summarizer is an AI-powered web app that fetches the latest news (India and World), summarizes it using Google's Gemini API, and allows text-to-speech, language translation (English/Hindi), and sharing via WhatsApp.

🧠 Features

• Fetch real-time news from News API  
• Summarize using Gemini (Google Generative AI)  
• Listen to summaries via text-to-speech  
• Choose language: English or हिंदी  
• Download summary as PDF  
• Share summary on WhatsApp  
• Chatbot integration for asking about trending topics

🚀 Live Deployment

App is live on Render:  
🔗 https://news-summarizer-u9kv.onrender.com

🛠️ Tech Stack

• Flask (Python)  
• HTML5 + CSS3 (Responsive Design)  
• JavaScript  
• Google Gemini API  
• News API  
• Render (Deployment)

📁 Project Structure

• `app.py` – Main backend logic  
• `templates/` – HTML files  
• `static/` – CSS & assets  
• `requirements.txt` – Python dependencies  
• `Procfile` – For Render deployment  
• `.env` – (Only for local testing) holds API keys

🔐 Environment Variables

Add the following keys in Render Dashboard under "Environment":

• `GOOGLE_API_KEY` → Your Gemini API key  
• `NEWS_API_KEY` → Your News API key

🔧 Local Setup Instructions

1. Clone the repository:  
   `git clone https://github.com/sanyagupta31/news_summarizer.git`

2. Navigate to the project:  
   `cd news_summarizer`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Create a `.env` file and add:

```

GOOGLE\_API\_KEY=your\_gemini\_api\_key
NEWS\_API\_KEY=your\_news\_api\_key

```

5. Run the app:  
`python app.py`

📦 Deployment (Render)

1. Push code to GitHub.
2. Go to [https://render.com](https://render.com) → New Web Service.
3. Connect your GitHub repo.
4. Add environment variables.
5. Build Command: (leave empty)  
Start Command: `python app.py`  
6. Hit Deploy!

👤 Author

Developed by Sanya Gupta  
GitHub: [sanyagupta31](https://github.com/sanyagupta31)  
Made with 💙 and a love for AI.




