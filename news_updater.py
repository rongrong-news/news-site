import openai
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatgpt_news():
    categories = [
        "latest world news",
        "latest US stock news",
        "latest China news",
        "latest China stock news",
        "latest Singapore news",
        "latest Singapore stock news",
        "latest technology development news"
    ]
    messages = [{"role": "system", "content": "You are a helpful assistant summarizing daily news."}]
    messages.append({"role": "user", "content": "Give me today's news summary in the following categories:
" + "\n".join(categories)})

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

def write_html(news_text):
    today = datetime.date.today().strftime("%Y-%m-%d")
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset='UTF-8'><title>Daily News {today}</title></head>
<body>
  <h1>📰 Daily News – {today}</h1>
  <div>{news_text.replace("\n", "<br><br>")}</div>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    news = get_chatgpt_news()
    write_html(news)