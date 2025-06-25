import openai
import os
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_news():
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes news."},
        {"role": "user", "content": (
            "Give me short daily news summaries in the following categories:\n"
            "1. World news\n2. US stock news\n3. China news\n4. China stock news\n"
            "5. Singapore news\n6. Singapore stock news\n7. Technology news"
        )}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content

def update_html(news_text):
    today = datetime.date.today().strftime("%Y-%m-%d")
    html = f"""<!DOCTYPE html>
<html lang='en'>
<head><meta charset='UTF-8'><title>News {today}</title></head>
<body>
  <h1>📰 News Summary – {today}</h1>
  <div>{news_text.replace("\n", "<br><br>")}</div>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    news = get_news()
    update_html(news)
