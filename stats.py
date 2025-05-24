def get_num_words(text):
    words = text.split()
    return len(words) 

def get_char_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sorted_char_count(dict):
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict

