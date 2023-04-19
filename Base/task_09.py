
def connect_dicts(dict1=None, dict2=None):
    filter_dict1 = dict()
    filter_dict2 = dict()
    summary1 = sum(dict1.values())
    summary2 = sum(dict2.values())

    for key, value in dict1.items():
        if value > 10:
            filter_dict1.update({key: value})
    for key, value in dict2.items():
        if value > 10:
            filter_dict2.update({key: value})

    if summary2 >= summary1:
        for priority_key in filter_dict2.keys():
            for key in list(filter_dict1.keys()):
                if priority_key == key:
                    filter_dict1.pop(key)
        priority_dictionary = dict(**filter_dict2, **filter_dict1)

    if summary1 > summary2:
        for priority_key in filter_dict1.keys():
            for key in list(filter_dict2.keys()):
                if priority_key == key:
                    filter_dict2.pop(key)
        priority_dictionary = dict(**filter_dict1, **filter_dict2)
    sorted_keys = sorted(priority_dictionary, key=priority_dictionary.get)
    out_dict = {}
    for w in sorted_keys:
        out_dict[w] = priority_dictionary[w]
    return out_dict


