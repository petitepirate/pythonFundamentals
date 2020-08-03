def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_dict = {letter : phrase.count(letter) for letter in phrase}
    return letter_dict

print(multiple_letter_count('hola que pasa'))
print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))

# --------------------------------------------------------
# School Solution

#     counter = {}

#     for ltr in phrase:
#         counter[ltr] = counter.get(ltr, 0) + 1

#     return counter
