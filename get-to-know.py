from flask import Flask, render_template
import json
import feedparser
import globalvoices

from tweets import country_tweets


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list())
    )

@app.route("/country/<country>")
def country(country):
    stories = globalvoices.recent_stories_from( country )
    tweet_list = country_tweets(country)
    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list()),
        country_name=country,
        stories=stories,
        tweets=tweet_list
    )
    
    return render_template("tweets.html", )

if __name__ == "__main__":
    app.debug = True
    app.run()
