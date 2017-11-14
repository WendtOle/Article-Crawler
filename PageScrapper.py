import requests
from bs4 import BeautifulSoup

class PageScrapper:

    domain = '' # usally "http://www.spiegel.de"

    def __init__(self,domain):
        self.domain = domain

    def getTitleOfArticle(self, pageURL):
        return pageURL.select('h2 span[class="headline"]')[0].text

    def getAuthorsOfArticle(self, pageURL):
        authors = ''
        allAuthors = pageURL.select('p[class="author"] a')

        for author in allAuthors:
            authors += ''.join(author.getText()) + ", "
        return authors

    def getTimeOfArticle(self, pageURL):
        unformattedTimeStamp = pageURL.select('time[class="timeformat"]')[0].getText().split()
        formattedTimeStamp = ''
        for element in unformattedTimeStamp:
            formattedTimeStamp += " " + ''.join(element)
        return formattedTimeStamp

    def caesarCypher(self, cypherText, move):
        plainText = ""
        for string in cypherText:
            if string is ' ':
                plainText += ' '
            else:
                if string is not '\n':
                    plainText += ''.join(chr(ord(string) + move))
        return plainText

    def getContent(self, pageContent):
        clearText = cypherText = ''

        for text in pageContent.select('div [class="article-section clearfix"] p'):
            if not text.get("class") and not text.find("strong"):
                clearText += ''.join(text.getText())

        for cypherElement in pageContent.findAll("p", {"class": "obfuscated"}):
            cypherText += ''.join(cypherElement.getText())

        completeText = clearText + self.caesarCypher(cypherText, -1)
        return completeText.replace('\n', ' ')

    def scrapPage(self, pathOfPage):
        soupOfFirstPage = BeautifulSoup(requests.get(self.domain + pathOfPage).content, 'html.parser')

        titleOfArticle = self.getTitleOfArticle(soupOfFirstPage)
        authors = self.getAuthorsOfArticle(soupOfFirstPage)
        timeOfArticle = self.getTimeOfArticle(soupOfFirstPage)
        clearText = self.getContent(soupOfFirstPage)

        return {'title': titleOfArticle, 'date': timeOfArticle, 'authors': authors, 'content': clearText}