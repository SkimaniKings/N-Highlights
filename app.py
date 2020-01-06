from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="cca440cda74d458a8d8d34a747f29ac8")