import requests
from bs4 import BeautifulSoup
import json
import sys
import time
class HTTPError(Exception):
    pass
class BooksToScrapeSpider:
    """
    A web scraping utility designed to extract book information from 
    books.toscrape.com, and save it to a JSON file for future analysis.
    """
    def __init__(self, output:str="output.json") -> None:
        self.__start = time.perf_counter()
        print("The spider is starting...")
        self._data = []
        self._output = output
    def _request(self,url:str) -> str:
        for _ in range(10):
            try:
                respond = requests.get(url)
                if respond.status_code != 200:
                    print(respond.status_code)
                    raise HTTPError()
                return respond.text
            except:
                time.sleep(5)
        sys.exit()
    def Scrape(self, url:str = "https://books.toscrape.com/catalogue/page-1.html") -> int:
        respond = self._request(url)
        soup = BeautifulSoup(respond, 'lxml')
        for book in soup.find_all("article", class_='product_pod'):
            href = book.h3.a["href"]
            page = self._request(f"https://books.toscrape.com/catalogue/{href}")
            self._process_page(page) 
        next = soup.find("li", class_="next")
        if not next:
            self._SaveToJson()
            end = time.perf_counter()
            print(f"Finished in {end-self.__start} seconds")
            return 0
        next = next.a["href"]
        if "catalogue" not in next:
            next = "catalogue/"+next
        self.Scrape(f"https://books.toscrape.com/{next}")
    def _SaveToJson(self) -> None:
        with open(self._output, "w") as j:
            js = json.dumps(self._data)
            j.write(js)
    def _process_page(self, page:str) -> None:
        try:
            page_data = {}
            soup = BeautifulSoup(page, 'lxml')
            page_data["title"] = soup.find("div", class_="col-sm-6 product_main").h1.text
            page_data["price"] = float(soup.find("p", class_="price_color").text.replace("£", "").replace("Â", ""))
            page_data["description"] = soup.find("div", attrs={"id":"product_description"}).find_all_next()[1].text.encode('latin1').decode('utf-8')
            page_data["number_of_stars"] = soup.select("p.star-rating")[0]["class"][1]
            page_data["genre"] = soup.select(".breadcrumb")[0].find_all_next()[5].text
            print(page_data)
        except: pass
        self._data.append(page_data)
spider = BooksToScrapeSpider()
spider.Scrape()