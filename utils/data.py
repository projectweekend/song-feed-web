from boto.dynamodb2.table import Table
from dates import date_to_timestamp


FEED_ITEMS = Table('feed_items')
ACCOUNTS = Table('accounts')


def feed_items(start, end):
    start = date_to_timestamp(start)
    end = date_to_timestamp(end)
    r = FEED_ITEMS.query_2(
        reverse=True,
        spotify_username__eq='musicman1381',
        date_posted__gte=start,
        date_posted__lte=end)
    return [dict(i.items()) for i in r]


def feed_info():
    r = ACCOUNTS.query_2(
        attributes=('feed_title', ),
        spotify_username__eq='musicman1381')
    return [dict(i.items()) for i in r].pop()
