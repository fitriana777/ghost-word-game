def is_complete_word(fragment, word_list):
    return fragment in word_list and len(fragment) >= 4

def is_valid_fragment(fragment, word_list):
    return any(word.startswith(fragment) for word in word_list)
