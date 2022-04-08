import requests
from bs4 import BeautifulSoup

url = 'https://www.ceneo.pl/91714422#tab=reviews'
response=requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")

opinion = opinions.pop(0)
opinion_id=opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
reccomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
stars = opinion.select_one("span.user-post__score-count").get_text()
content = opinion.select_one("div.user-post__text").get_text()
useful = opinion.select_one('span[id^="votes-yes"]').get_text().strip()
useless = opinion.select_one('|span[id^="votes-no"]')
publish_date = opinion.select_one('span.user-post__published > time:nth-child(1)'["datetime"])
purchase_date = opinion.select_one('span.user-post__published > time:nth-child(2)'["datetime"])

print(publish_date)