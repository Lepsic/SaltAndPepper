def sort_list(input_data: list) -> list:
    if input_data == list():
        return input_data
    min_value = min(input_data)
    max_value = max(input_data)
    for element in range(len(input_data)):
        if input_data[element] == min_value:
            input_data[element] = max_value
            continue
        if input_data[element] == max_value:
            input_data[element] = min_value
            continue
    input_data.append(min_value)
    return input_data



