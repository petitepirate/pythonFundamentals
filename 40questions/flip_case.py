def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """


# My solution:
    new_phrase = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.upper()
            new_phrase += ltr
        if ltr.upper() == to_swap:
            ltr = ltr.lower()
            new_phrase += ltr
        new_phrase += ltr
    return new_phrase


print(flip_case('Aaaahh', 'a'))  # prints AAAAAhh
print(flip_case('Aaaahh', 'A'))  # prints aaaaahh
print(flip_case('Aaaahh', 'h'))  # prints AaaaHH
# _______________________________________________________
# School Solution

#  to_swap = to_swap.lower()
#   out = ""

#    for ltr in phrase:
#         if ltr.lower() == to_swap:
#             ltr = ltr.swapcase()
#         out += ltr

#     return out


# print(flip_case('Aaaahh', 'a'))   # prints aAAAhh
# print(flip_case('Aaaahh', 'A'))   # prints aAAAhh
# print(flip_case('Aaaahh', 'h'))   # prints AaaaHH
