# Write your code here
import re


def parse_link(string):
    match = re.fullmatch(r"<a href=\"(.*)\">(.*)</a>", string)

    if match:
        link, caption = match.groups()
        link_and_caption = (caption, link)
        return link_and_caption

    return None
