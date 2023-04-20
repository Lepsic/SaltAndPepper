def multiply_numbers(inputs=None):
    output_value = 1
    if inputs is None:
        return None
    check_value = False
    inputs = str(inputs)
    for elements in inputs:
        if type(elements) == str:
            try:
                elements = int(elements)
                check_value = True
                output_value *= elements
            except ValueError:
                continue
    if not check_value:
        return None
    return output_value



