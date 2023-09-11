def multiple_returns(sentence):

    sentence_len = len(sentence)

    if sentence_len == 0:
        f_char = None
    else:
        f_char = sentence[0]

    t = (sentence_len, f_char)

    return (t)
