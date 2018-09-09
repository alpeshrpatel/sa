import feedparser
import pymongo
from pymongo import MongoClient

connection = pymongo.MongoClient("mongodb://localhost")


# List of RSS feeds that we will fetch and combine
newsurls = {
    'apnews':           'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
    'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
    'yahoonews':        'http://news.yahoo.com/rss/'
}
 
 
# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
    
    return headlines
 

def readNewsURL( ):
    # A list to hold all headlines
    allheadlines = []    
    # Iterate over the feed urls
    for key,url in newsurls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allheadlines.extend( getHeadlines( url ) )
    # Iterate over the allheadlines list and print each headline
    # for hl in allheadlines:
    #     print(hl)
    insertInToMongo(allheadlines)
    return



def insertInToMongo(allheadlines):
    # get a handle to the reddit database
    db = connection.news
    news = db.news
    for hl in allheadlines:
        # print(hl)
        news.insert_one({"title":hl})
    # put it in mongo
    return
            

if __name__ == "__main__":
   readNewsURL()    
 
 
# end of code 