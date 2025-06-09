# Write your code here
import re


def collect_links(string):
    links = re.findall(r"href=\"(.*)\"", string)

    if links:
        return links
    return None
