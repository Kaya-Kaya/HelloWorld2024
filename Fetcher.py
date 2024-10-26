import feedparser
from newspaper import Article

rss_links = {
    'nytimes': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'cnn': 'http://rss.cnn.com/rss/cnn_latest.rss/',
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'washingtonpost': 'http://feeds.washingtonpost.com/rss/world',
    'abcnews': 'http://abcnews.go.com/abcnews/topstories',
    'nbcnews': 'http://feeds.nbcnews.com/nbcnews/public/news',
    'cbsnews': 'http://www.cbsnews.com/latest/rss/main',
    'buzzfeed': 'https://www.buzzfeed.com/world.xml',
    'vice': 'https://www.vice.com/en/feed/?locale=en_us',
    'slate': 'http://www.slate.com/rss',
    'vox': 'http://www.vox.com/rss/index.xml',
    'salon': 'http://www.salon.com/feed/',
    'theintercept': 'https://theintercept.com/feed/?rss',
    'theatlantic': 'http://feeds.feedburner.com/TheAtlantic',
    'thenewyorker': 'http://www.newyorker.com/feed/news',
    'time': 'http://feeds2.feedburner.com/time/topstories',
    'businessinsider': 'http://www.businessinsider.com/rss',
    'fortune': 'http://fortune.com/feed/',
    'cnbc': 'http://www.cnbc.com/id/100003114/device/rss/rss.html',
    'latimes': 'http://www.latimes.com/local/rss2.0.xml',
    'democracynow': 'https://www.democracynow.org/democracynow.rss',
    'commondreams': 'https://www.commondreams.org/feeds/news.rss',
    'aljaazeera': 'http://www.aljazeera.com/xml/rss/all.xml',
    'propublica': 'https://www.propublica.org/feeds/propublica/main',
    'novaramedia': 'http://novaramedia.com/feed/',
    'guardian' : 'https://www.theguardian.com/world/rss',
}

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    print(feed)
    for entry in feed.entries:
        try:
            # create a newspaper article object
            article = Article(entry.link)
            print(entry.link)
            # download and parse the article
            article.download()
            article.parse()
            # extract relevant information
            articles.append({
                'title': article.title,
                'author': article.authors,
                'publish_date': article.publish_date,
                'content': article.text,
                'images' : article.images,
                'url': article.url
            })
        except Exception as e:
            pass
    return articles

def scrape_news_from_source(source):
    return scrape_news_from_feed(rss_links[source])

# articles = scrape_news_from_source('guardian')

# # print the extracted articles
# for article in articles:
#     print('Title:', article['title'])
#     print('Author:', article['author'])
#     print('Publish Date:', article['publish_date'])
#     print('Content:', article['content'])
#     print('Images:', article['images'])
#     print('URL:', article['url'])
#     print()
