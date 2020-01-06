from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="28d135ff8b27447caf2f3b7cd13fb15a")
    topheadlines = newsapi.get_top_headlines(sources="abc-news-au")
    
    articles = topheadlines['articles']
     
    des=[]
    image=[]
    news=[]
    pubAt=[]
    url= []
    
  
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        des.append(myarticles['description'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
 
        
    mylist=zip(des,image,news,pubAt,url)
    return render_template('index.htm', context = mylist)
if __name__ == "__main__":
    app.run(debug=True)
        
 