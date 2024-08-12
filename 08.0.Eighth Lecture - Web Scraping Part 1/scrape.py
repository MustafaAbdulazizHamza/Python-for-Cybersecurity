# python3 -m pip install requests bs4 lxml
from bs4 import BeautifulSoup

with open("simple_web_page.html") as h:
    soup = BeautifulSoup(h.read(), "lxml")
    # print(soup.prettify())
    title = soup.head.title.text
    print(title)
    article1_url = soup.body.div.h2.a.attrs["href"]
    print(article1_url)
    print(soup.find("div", class_="footer").p.text)
    articles = soup.find_all('div', class_='article')
    data = {}
    for article in articles:
        head = article.a.text
        link = article.h2.a.attrs["href"]
        summery = article.p.text
        data[head] = [link, summery]
    print(data)