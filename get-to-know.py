from flask import Flask, render_template, g
import json
import feedparser
import globalvoices
import sqlite3

from tweets import country_tweets
from world_db import connect_db
from world_db import query_db
from world_db import DATABASE

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route("/")
def index():
    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list())
    )

@app.route("/country/<country>")
def country(country):
    stories = globalvoices.recent_stories_from( country )
    tweet_list = country_tweets(country)

    country_entry = query_db('select * from Country where Name = ?', [country], one=True)
    language = query_db('select Language from CountryLanguage where CountryCode = ?', [country_entry['Code']], one=True)

    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list()),
        country_name=country,
        stories=stories,
        tweets=tweet_list,
        language=language,
        population=country_entry['Population']
    )
    
    return render_template("tweets.html", )

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == "__main__":
    app.debug = True
    app.run()
