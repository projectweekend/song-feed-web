from boto.dynamodb2.table import Table
from dates import date_to_timestamp


FEED_ITEMS = Table('feed_items')


def feed_data(start, end):
    start = date_to_timestamp(start)
    end = date_to_timestamp(end)
    r = FEED_ITEMS.query_2(
        reverse=True,
        spotify_username__eq='musicman1381',
        date_posted__gte=start,
        date_posted__lte=end)
    return [dict(i.items()) for i in r]
