Flask Example - Get To Know : Global Voices
===========================================

Small example Flask applicaton for the MAS.s60 course.
Added a twitter feed for the country at the bottom of the page (Using code from: https://github.com/jspeis/movieslikednow)
Added country info read from a database.

Installation
------------

Make sure you have Python 2.7 (and the pip package manager).

You also need to install the flask, feedparser and tweepy libraries

```
pip install flask
pip install feedparser
pip install tweepy
```

Build the database using this SQLite command:
.read data/world.sql

Use
---

Run this command and then visit `localhost:5000` with a web browser

```
python get-to-know.py
```
