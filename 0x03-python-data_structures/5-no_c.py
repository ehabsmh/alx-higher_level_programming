#!/usr/bin/python3
def no_c(my_string):

    my_string_list = ['' if s == 'c' or s == 'C'
                      else s for s in my_string]
    return (''.join(my_string_list))
