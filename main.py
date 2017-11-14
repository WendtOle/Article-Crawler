import requests
from bs4 import BeautifulSoup

from PageScrapper import PageScrapper
from DatabaseHandler import DatabaseHandler

handler = DatabaseHandler('sqlite:///spiegelArticles.db')
scrapper = PageScrapper("http://www.spiegel.de")

def gatherSpiegelPlusArticleLinks(maxAmountOfLinks, startPage):
    links = []
    while len(links) < maxAmountOfLinks:
        listPageSoup = BeautifulSoup(requests.get(startPage).content, 'html.parser')
        for link in listPageSoup.select('h2 a[href]'):
            links.append(link.get('href'))
        currentListPage = "http://www.spiegel.de" + listPageSoup.select('div a[class="link-right"]')[0].get('href')
    return links

links = gatherSpiegelPlusArticleLinks(10,'http://www.spiegel.de/spiegelplus/')
for link in links:
    scrapedPage = scrapper.scrapPage(link)
    handler.addArticle(scrapedPage)
    print(scrapedPage)
print('finished')