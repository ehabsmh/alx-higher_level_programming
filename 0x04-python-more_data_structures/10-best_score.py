#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        best_key = ""
        maximum = 0
        for k, v in a_dictionary.items():
            if v >= maximum:
                best_key = k
                maximum = v

        return best_key

    return None
