from datetime import date
from datetime import timedelta
from flask import render_template
from server import app
from utils.data import feed_items, feed_info


@app.route('/')
def home():
    end = date.today()
    start = end - timedelta(days=7)
    return render_template(
        'home.html',
        feed_info=feed_info(),
        feed_items=feed_items(start, end))
