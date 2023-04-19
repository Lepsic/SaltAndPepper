import re
from collections import Counter

exception_string = "-"


def count_words(input_str: str):
    input_str = input_str.lower()
    input_str_update = re.sub(exception_string, "", input_str)
    str_array = input_str_update.split()
    counter = Counter(str_array)
    return dict(counter)


