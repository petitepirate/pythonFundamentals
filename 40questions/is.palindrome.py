def remove(phrase): 
    phrase = phrase.replace(" ", "")
    return phrase

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    new_phrase = remove(phrase).lower(),
    if new_phrase == new_phrase[::-1]:
        return True

print(is_palindrome('taco cat'))

print(is_palindrome('Noon'))

# ----------------------------------------------
# school solution:

#     normalized = phrase.lower().replace(' ', '')
#     return normalized == normalized[::-1]
