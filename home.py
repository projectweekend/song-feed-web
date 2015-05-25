from datetime import date
from datetime import timedelta
from flask import render_template
from server import app
from utils.data import feed_data


@app.route('/')
def home():
    end = date.today()
    start = end - timedelta(days=7)
    feed_items = feed_data(start, end)
    return render_template('home.html', feed_items=feed_items)
