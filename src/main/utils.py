
from datetime import datetime


S_IN_DAY = 86400
S_IN_HOUR = 3600
S_IN_MINUTE = 60


def str2date(str, format="%d%m%y"):
    return datetime.strptime(str, format)


def humanize_date(seconds):
    def convert_seconds(seconds):
        d = seconds//S_IN_DAY
        h = (seconds % S_IN_DAY) // S_IN_HOUR
        m = (seconds % S_IN_HOUR) //S_IN_MINUTE
        return (d, h, m)

    d, h, m = convert_seconds(seconds)

    d = '{}d '.format(d) if d else ''
    h = '{}h '.format(h) if h else ''
    m = '{}m'.format(m) if m else ''
    return ''.join([d, h, m])
