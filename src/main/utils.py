
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


def indent(text, n=4):
    if not text:
        return ""
    i = " " * n
    return i + text.replace("\n", "\n" + i)


def json_escape(s):
    if isinstance(s, bool):
        return "true" if s else "false"
    if s is None:
        return ""
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


class PrettyJSON(object):
    @classmethod
    def to_json(cls, o, order=None):
        r = cls.convert(o, 0, order)
        if not r.endswith("\n"):
            r += "\n"
        return r

    @classmethod
    def convert(cls, o, i, order=None):
        if o is None:
            return indent("null", i)
        if isinstance(o, six.string_types):
            return indent('"%s"' % json_escape(o), i)
        elif isinstance(o, bool):
            return indent("true" if o else "false", i)
        elif isinstance(o, six.integer_types):
            return indent("%d" % o, i)
        elif isinstance(o, float):
            return indent(str(o), i)
        elif isinstance(o, uuid.UUID):
            return indent('"%s"' % o, i)
        elif isinstance(o, list):
            if len(o) == 0:
                return indent("[]", i)
            t = [cls.convert(e, 0, order) for e in o]
            lt = reduce(lambda x, y: x + y, [len(x) for x in t])
            lt += i + (len(o) - 1) * 2
            if lt > 72:
                # Long line
                r = [indent("[", i)]
                r += [",\n".join(indent(x, i + 4) for x in t)]
                r += [indent("]", i)]
                return "\n".join(r)
            else:
                r = "[%s]" % ", ".join(t)
                return indent(r, i)
        elif isinstance(o, dict):
            if not o:
                return indent("{}", i)
            keys = sorted(o)
            if order:
                nk = [k for k in order if k in keys]
                nk += [k for k in keys if k not in order]
                keys = nk
            r = ",\n".join("%s: %s" % (cls.convert(k, 0), cls.convert(o[k], 0)) for k in keys)
            return indent("{\n%s\n}" % indent(r, 4), i)
        raise ValueError("Cannot encode %r" % o)


to_json = PrettyJSON.to_json
