# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from re import search

class ScrapyfwdemoPipeline:
    def process_item(self, item, spider):
        return item
class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for field_name in adapter.field_names():
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip().replace('"', '').replace("'", "")
        # To make the genre string lowercase
        value = adapter.get('genre')
        adapter['genre'] = value.lower()
        # All price data should be float
        price_data = ['Price_exc_tax', 'price_inc_tax', 'tax']
        for pr in price_data:
            value = adapter.get(pr)
            adapter[pr] = float(value.replace('£', ''))

        # To extract the number of books that are available
        value = adapter.get('availability')
        r = search('\d+', value)
        if r:
            value = int(r.group())
            adapter['availability'] = value
        else:
            adapter['availability'] = 0
        # Number of reviews should be integer
        value  = adapter.get("number_of_reviews")
        adapter['number_of_reviews'] = int(value)
        # To convert number of stars to int rather than a text:
        numbers = ['zero','one', 'two', 'three', 'four', 'five']
        value = adapter.get('number_of_stars')
        if value.lower() in numbers:
            number = numbers.index(value.lower())
            adapter['number_of_stars'] = int(number) 
        return item
