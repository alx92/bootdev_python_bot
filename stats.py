def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    count_char = {}
    text = text.lower()
    for ch in text:
        count_char[ch] = count_char.get(ch, 0) + 1
    return count_char

def sort_on(items):
    return items.get("num")

def build_report(dict_list):
    items = []

    for k, v in dict_list.items():
        items.append({"char":k, "num":v})

    return items
