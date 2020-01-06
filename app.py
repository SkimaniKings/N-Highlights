from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
  """
 A view root page function that returns the index page and its data
  """