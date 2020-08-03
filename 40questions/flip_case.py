def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
            out += ltr
        else:
            return ltr
        if ltr.upper() == to_swap:
            ltr = ltr.swapcase()
            out += ltr
        else: 
            return ltr

    return out

print(flip_case('Aaaahh', 'a'))
print(flip_case('Aaaahh', 'A'))
print(flip_case('Aaaahh', 'h'))
