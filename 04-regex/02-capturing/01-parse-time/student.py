import re


def parse_time(string):
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)

    if match:
        h, m, s, ms = match.groups("0")
        ms = ms[1:]
        ms = ms or 0
        hours_and_shit = (int(h), int(m), int(s), int(ms))
        return hours_and_shit
    return None