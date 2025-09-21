    
def count_words(text):
    word_count = len(text.split())
    return word_count

def char_count(text):
    characters = {}
    for char in (text.lower()):
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_char_counts(characters):
    char_list = [{"char": k, "num": v} for k, v in characters.items()]
    def get_num(item):
        return item["num"]
    char_list.sort(key=get_num, reverse=True)
    return char_list
