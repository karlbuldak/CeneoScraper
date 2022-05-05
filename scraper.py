from encodings import utf_8
import requests
import json
from bs4 import BeautifulSoup
#zmien zeby bylo na input urla 
url = input("Wprowadź link do produktu: ")
numeric_filter = filter(str.isdigit, url)
numeric_string = "".join(numeric_filter)
all_opinions = []
while(url):
    response=requests.get(url)

    page = BeautifulSoup(response.text, 'html.parser')

    opinions = page.select("div.js_product-review")
    for opinion in opinions:        
        opinion_id=opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            reccomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            reccomendation = None
        stars = opinion.select_one("span.user-post__score-count").get_text()
        content = opinion.select_one("div.user-post__text").get_text()
        useful = opinion.select_one('span[id^="votes-yes"]').get_text().strip()
        useless = opinion.select_one('|span[id^="votes-no"]')
        publish_date = opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]
        try:
            purchase_date = opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]
        except TypeError:
            purchase_date = None
        pros = opinion.select('div[class$="positives"]~div.review-feature__item')
        proslist = [item.get_text().strip() for item in pros]

        cons = opinion.select('div[class$="negatives"]~div.review-feature__item')
        conslist = [item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "reccomendation": reccomendation,
            "stars": stars,
            "content": content,
            "useful": useful,
            "useless": useless,
            "publish_date": publish_date,
            "purchase_date": purchase_date,
            "pros":proslist,
            "cons": conslist
        }
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl" + page.select_one('a.pagination_next')['href']
    except TypeError:
        url = None


    with open("opinions/" + numeric_string + ".json", 'w', encoding='UTF_8') as jf:
        json.dump(all_opinions, jf, indent=4, ensure_ascii=False)