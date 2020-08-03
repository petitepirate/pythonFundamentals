def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    x = letter.lower()
    return word.lower().count(x)


print(single_letter_count('hello', 'h'))
print(single_letter_count('Hello World', 'z'))
print(single_letter_count("Hello World", 'l'))

#------------------------------------------------
# School Solution

#   return word.lower().count(letter.lower())
