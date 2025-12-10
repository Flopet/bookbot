def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    character_count = {}
    lowered = text.lower()
    characters = list(lowered)

    for char in characters:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count



def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list