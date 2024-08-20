import scrapy
from ScrapyFWDemo.items import BookItem

class BooksspiderSpider(scrapy.Spider):
    name = "BooksSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            book_page = book.css('h3 a').attrib['href']
            if 'catalogue' not in book_page:
                book_page = 'catalogue/' + book_page
            book_page = 'https://books.toscrape.com/' + book_page
            yield response.follow(book_page, callback=self.parse_book_page)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            if 'catalogue' not in next_page:
                next_page = "catalogue/" + next_page
            full_next_page_url = 'https://books.toscrape.com/' + next_page
            yield response.follow(full_next_page_url, callback=self.parse)
    def parse_book_page(self, response):
        book_item = BookItem()
        
        book_item['url'] = response.url
        book_item['title'] =  response.css('.product_main h1::text').get()
        book_item['upc'] = response.css("table tr td::text")[0].get()
        book_item['Price_exc_tax'] =  response.css("table tr td::text")[2].get()
        book_item['price_inc_tax']  = response.css("table tr td::text")[3].get()
        book_item['tax'] =  response.css("table tr td::text")[4].get()
        book_item['availability']  =  response.css("table tr td::text")[5].get()
        book_item['number_of_reviews']  = response.css("table tr td::text")[6].get()
        book_item["number_of_stars"]  =  response.css("p.star-rating").attrib['class'].split()[1]
        book_item['description'] =  response.xpath('//div[@id = "product_description"]/following-sibling::p/text()').get()
        book_item['genre']  = response.xpath("//ul [@class = 'breadcrumb']/li [@class = 'active']/preceding-sibling::li[1]/a/text()").get()

        yield book_item