from collections import Counter


def combine_anagrams(words_array):
    counter_list = list()
    out_data = list()
    for word in words_array:
        counter_list.append(Counter(word))

    for current_counter in range(len(counter_list)):
        append_list = [words_array[current_counter]]
        for counter in range(len(counter_list)):
            if counter_list[current_counter] == counter_list[counter]:
                if words_array[counter] in append_list: # проверка на существование повторяющихся элементов в массиве добавления
                    continue
                append_list.append(words_array[counter])
        for append_elements in append_list: # проверка на повторяющиеся элекменты
            for out_elements in out_data:
                if append_elements in out_elements:
                    append_list = list()
                    break
        if append_list != list(): # Исключение добавлений пустых массивов
            out_data.append(append_list)

    return out_data


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))
