import re
from collections import Counter

alphavit = set("1234567890qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM")




def count_words(input_str: str):
    input_str = ''.join(filter(alphavit.__contains__, input_str)).lower()
    str_array = input_str.split()
    counter = Counter(str_array)
    return dict(counter)


print(count_words("A man, a plan, a canal -- Panama"))

