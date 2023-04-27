def max_odd(array: list):
    sort_array = list()
    max_value = None
    for element in array:
        try:
            element = float(element)
            if element % 2 != 0:
                sort_array.append(element)
            else:
                continue
        except ValueError:
            continue
    if len(sort_array) != 0:
        max_value = max(sort_array)
        if max_value % 1 == 0:
            return int(max_value)
        else:
            return max_value
    else:
        return max_value




print(max_odd(['ololo', 'fufufu']))