import random
from utils import is_valid_fragment

def get_ai_move(fragment, word_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    valid_moves = []

    for letter in alphabet:
        test = fragment + letter
        if is_valid_fragment(test, word_list):
            valid_moves.append(letter)

    return random.choice(valid_moves) if valid_moves else random.choice(alphabet)
