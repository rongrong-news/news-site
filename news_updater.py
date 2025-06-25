import openai
import datetime
import os

# Get API key from environment variable (for GitHub Actions)
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_news():
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional news summarizer."},
            {"role": "user", "content": "Give me a 3-paragraph summary of today’s top tech and world news. Keep it concise, informative, and web-friendly."}
        ]
    )
    return response['choices'][0]['message']['content']

def update_html(news_text):
    # Replace line breaks with HTML <br> tags
    html_content = news_text.replace('\n', '<br><br>')

    html_template = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Daily News Summary</title>
</head>
<body>
  <h1>📰 Daily News — {datetime.date.today().strftime('%B %d, %Y')}</h1>
  <div>{html_content}</div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    news = get_news()
    update_html(news)
