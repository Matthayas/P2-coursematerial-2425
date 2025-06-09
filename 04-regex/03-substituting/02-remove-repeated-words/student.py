# Write your code here
import re


def remove_repeated_words(string):
    new_string = re.sub(r"\b(\w+)\b(\s+\b\1\b)*", r"\1", string)
    return new_string
