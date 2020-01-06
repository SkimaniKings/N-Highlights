from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="9928e2b4e73e42319e3b5832e0c6c672")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")
    
    articles = topheadlines['articles']
    
    heading= []
    news = []
    image = []
    date = []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        heading.append(myarticles['title'])
        news.append(myarticles['description'])
        image.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        
        mylist = zip(heading,news,image,date)
        
        return render_template('index.htm', context = mylist)
if __name__ == "__main__":
    app.run(debug=True)
        
 