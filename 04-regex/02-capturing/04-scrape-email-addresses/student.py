# Write your code here
import re


def scrape_email_addresses(string):
    addresses = re.findall(r"[a-z\d.]+@[a-z\d]+\.[a-z\d]+", string)

    if addresses:
        return addresses
    return None
