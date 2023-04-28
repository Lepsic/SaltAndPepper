
def coincidence(data=None, rang=None) -> list:
    if data is None or rang is None:
        return list()
    if type(rang) is not range:
        raise TypeError("Второй аргумент не является объектом класса range")

    min_value = rang.start
    max_value = rang.stop
    out_array = list()
    for element in data:
        try:
            append_data = float(element)
            if max_value >= append_data >= min_value:
                if append_data % 1 == 0:
                    append_data = int(append_data)
                out_array.append(append_data)
        except ValueError:
            continue
        except TypeError:
            continue
    return out_array

