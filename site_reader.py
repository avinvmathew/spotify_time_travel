import requests
from bs4 import BeautifulSoup

class Billboard:
    def __init__(self):

        header = {
                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
                }
        url = "https://www.billboard.com/charts/hot-100/"

        response = requests.get(url=f"{url}", headers=header)
        content = response.text

        soup = BeautifulSoup(content,"html.parser")
        # print(soup.prettify())

        titles = soup.select("li.o-chart-results-list__item h3.c-title")
        self.titles_arr = [headings.getText(strip=True) for headings in titles]
        print(self.titles_arr)
    def get_song_list(self):
        return self.titles_arr

# # testing
# Billboard()