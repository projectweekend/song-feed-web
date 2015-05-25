from time import mktime


def date_to_timestamp(d):
    return int(mktime(d.timetuple()))
