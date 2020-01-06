from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="6530e4aa762c497d83c8aa95953c3750")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

 
        
        mylist = zip(news, desc, img)
        
        return render_template('index.htm', context = mylist)
if __name__ == "__main__":
    app.run(debug=True)
        
 