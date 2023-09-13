#!/usr/bin/python3
def best_score(a_dictionary):

    if type(a_dictionary) is not dict:
        return None

    best_key = ""
    maximum = 0
    for k, v in a_dictionary.items():
        if v >= maximum:
            best_key = k
            maximum = v

    return best_key
