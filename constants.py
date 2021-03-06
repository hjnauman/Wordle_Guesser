import json

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
VIABLE_WORDS = json.load(open('word_list.json', 'r'))
LETTER_FREQUENCIES = {
    'a': 8.193,
    'b': 1.524,
    'c': 3.291,
    'd': 3.706,
    'e': 12.059,
    'f': 2.143,
    'g': 2.030,
    'h': 4.832,
    'i': 7.546,
    'j': 0.179,
    'k': 0.732,
    'l': 4.170,
    'm': 2.567,
    'n': 7.142,
    'o': 7.520,
    'p': 2.158,
    'q': 0.125,
    'r': 6.012,
    's': 6.633,
    't': 9.324,
    'u': 3.040,
    'v': 1.061,
    'w': 1.717,
    'x': 0.246,
    'y': 1.938,
    'z': 0.115
}
