import pandas as pd
from newspaper import Article
import os.path

# Function to extract article data
def extract_article_data(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    data = {
        'Title': article.title,
        'Text': article.text,
        'Keywords': ', '.join(article.keywords),
        'URL': url
    }
    return data

if __name__ == "__main__":
    extract_article_data()
    