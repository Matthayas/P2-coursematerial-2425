# Write your code here
import re


def is_valid_student_id(string):
    if re.fullmatch("[rsRS]\d{7}", string):
        return True
    return False