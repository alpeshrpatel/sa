import feedparser as fp
from pandas import json
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

# Set the limit for number of articles to download
LIMIT = 4

data = {}
data['newspapers'] = {}

# Loads the JSON files with news sites
with open('NewsPapers.json') as data_file:
    companies = json.load(data_file)
    print(companies)