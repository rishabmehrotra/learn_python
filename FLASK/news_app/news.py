import feedparser
from flask import Flask, render_template
     
#creates an instance of the Flask object using our module's name as a parameter.
app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}
#Python decorator used by flask to invoke the function below when user opens the root page of the web application
@app.route('/')
def news():
    return("""
    1) /bbc
    2) /cnn
    3 /iol""") 

@app.route("/bbc")
def bbc():
    return get_news('bbc')
@app.route("/cnn")
def cnn():
    return get_news('cnn')
@app.route("/fox")
def fox():
    return get_news('fox')
@app.route("/iol")
def iol():
    return get_news('iol')
def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    #first_article = feed['entries'][0]
    return(render_template("front.html",articles=feed['entries']))


#It is used to prevent Python scripts from being unintentionally run when they are imported into other Python files.
if __name__ == '__main__':
    app.run(port=5000, debug =True) #We set it to run on port 5000 (we'll use port 80 for production) and set debug to True, which will help us see detailed errors directly in our web browser.