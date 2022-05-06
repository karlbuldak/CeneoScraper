# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://wwww.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.elementTag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja|span.user-post__author-recomendation > em|reccomendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$="positives"]~div.review-feature__item|pros||
|lista wad|div[class$="negatives"]~div.review-feature__item|cons||
|dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||

## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podania kodu produktu przez użytkownika
7. Optymalizacja kodu
    a. stworzenie funkcji do ekstrakcji elementów
    b. utworzenie słownika selektorów
    c. użycie dictionary comprehension do pobrania składowych pojedyńczej opinii na podstawie słownika selektorów

