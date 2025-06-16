import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {"title":[], "description":[], "publish":[]}

url = "https://www.dawn.com/latest-news"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = soup.select("a.story__link")
descriptions = soup.select("div.story__excerpt.font-georgia.text-3\\.5.text-gray-700.overflow-hidden.pb-1.px-0.sm\\:px-2.mt-0")
published = soup.select("span.timestamp--time.timeago")

for i in range(min(len(titles), len(descriptions), len(published))):
    title = titles[i].get_text(strip=True)
    description = descriptions[i].get_text(strip=True)
    publish = published[i].get_text(strip=True)

    print(title)
    print(description)
    print(publish)
    print("-" * 50)

    data["title"].append(title)
    data["description"].append(description)
    data["publish"].append(publish)

df = pd.DataFrame(data)
df.to_csv("news.csv", index=False)
df.to_excel("news.xlsx", index=False)

print("Scrapping is Completed")
