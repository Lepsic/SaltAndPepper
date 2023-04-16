def is_palindrome(input_data: str) -> bool:
    revere_str = input_data[::-1]
    if revere_str == input_data:
        return True
    else:
        return False
