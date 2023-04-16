def sort_list(input_data: list) -> list:
    min_value = min(input_data)
    max_value = max(input_data)
    max_index = len(input_data) - input_data[::-1].index(max_value)-1
    input_data[input_data.index(min(input_data))] = max_value
    input_data[max_index] = min_value
    input_data.append(min_value)
    return input_data



