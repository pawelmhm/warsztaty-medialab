
import json
import requests
from scrapy import Selector

def main():
    res = requests.get("https://www.bn.org.pl/")
    sel = Selector(text=res.text)
    news_entries = sel.css('#news .col-12.col-lg-4')
    output = []
    for news in news_entries:
        title = news.css('h3::text').get()
        link = news.css('.link::attr(href)').get()
        obj = {
            'title': title,
            'link': link
        }
        output.append(obj)

    with open('bn_news.json', 'w') as f:
        json.dump(output, f)


if __name__ == "__main__":
    main()