import requests
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ✅ Securely fetch API keys
News_api_key = os.getenv("NEWS_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# ✅ Configure Gemini
genai.configure(api_key=google_api_key)


def clean_summary(text):
    lines = text.split('\n')
    cleaned = [line.lstrip("*-• ").strip() for line in lines if line.strip()]
    return "\n\n".join(cleaned)


# ✅ Used for chatbot (topic-based news fetch)
def fetch_news(query="india", last24=True):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "sortBy": "publishedAt" if last24 else "relevancy",
        "pageSize": 10,
        "apiKey": News_api_key
    }
    res = requests.get(url, params=params)
    return res.json().get("articles", [])


# ✅ Used for homepage summary
def get_top_news(country="in", last24=False):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "pageSize": 10,
        "apiKey": News_api_key
    }

    if country == "in":
        params["country"] = "in"
        res = requests.get(url, params=params)
        articles = res.json().get("articles", [])

        if not articles:
            print("🔁 Retrying with q=india instead of country=IN")
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": "india",
                "sortBy": "publishedAt" if last24 else "relevancy",
                "pageSize": 10,
                "apiKey": News_api_key
            }
            res = requests.get(url, params=params)
            articles = res.json().get("articles", [])
    else:
        params["country"] = country
        res = requests.get(url, params=params)
        articles = res.json().get("articles", [])

    if not articles:
        print(f"⚠️ No articles returned for query: {country} with filters last24={last24}")
    return articles


def summarize_with_gemini(articles, lang="en", trending=False):
    headlines = "\n".join([f"- {article['title']}" for article in articles])
    language_instruction = "Respond in Hindi." if lang == "hi" else "Respond in English."
    extra = "Identify trending topics and combine related headlines." if trending else ""

    prompt = f"""
You are a smart news summarizer.
Summarize the following top news headlines in clean, concise language (no bullet points). 
{extra}
{language_instruction}

{headlines}
"""

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return clean_summary(response.text or "Gemini did not return a valid summary.")


# ✅ API route for summarized homepage news
@app.route("/summarize_news")
def summarize_news():
    try:
        country = request.args.get("country", "in")
        lang = request.args.get("lang", "en")
        last24 = request.args.get("last24", "false").lower() == "true"
        trending = request.args.get("trending", "false").lower() == "true"

        articles = get_top_news(country, last24)
        summary = summarize_with_gemini(articles, lang, trending)
        return jsonify({"summary": summary})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"summary": f"❌ Error occurred: {str(e)}"}), 500


# ✅ Chatbot endpoint
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()
    lang = data.get("lang", "en")

    try:
        # Detect topic (simplified logic)
        if "cricket" in user_message or "क्रिकेट" in user_message:
            query = "indian cricket team"
        else:
            query = "india"

        articles = fetch_news(query=query, last24=True)

        language_instruction = "Reply in Hindi." if lang == "hi" else "Reply in English."

        prompt = f"""
You are a smart news chatbot. Summarize the latest news about this user question:
"{user_message}"

Here are some top news headlines:
{chr(10).join([f"- {a['title']}" for a in articles])}

{language_instruction}
Avoid bullet points. Keep it short and simple (3-5 lines).
"""

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        reply = clean_summary(response.text or "Sorry, no news available.")
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"❌ Error: {str(e)}"})

# ✅ Home route (index.html)
@app.route("/")
def home():
    return render_template("index.html")


# ✅ Chatbot UI route (chatbot_page.html)
@app.route("/chatbot_page")
def chatbot_page():
    return render_template("chatbot_page.html")


import os  # 👈 zaroori hai

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=int(os.environ.get("PORT", 5000)), 
        debug=True
    )
