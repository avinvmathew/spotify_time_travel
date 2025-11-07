import requests
from bs4 import BeautifulSoup

# year = input("Which year do you want to travel to (YYYY-MM-DD) ?")
header = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=f"{URL}", headers=header)
content = response.text

soup = BeautifulSoup(content,"html.parser")
# print(soup.prettify())

titles = soup.select("li.o-chart-results-list__item h3.c-title")
titles_arr = [headings.getText(strip=True) for headings in titles]
print(titles_arr)





