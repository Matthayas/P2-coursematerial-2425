# Write your code here
#for all the European weirdos who don't know we refer to dates as February 1st not 1st of February
import re


def correct_dates(string):
    new_date = re.sub(r"(\d+)/(\d+)/(\d+)", r"\2/\1/\3", string)
    return new_date
