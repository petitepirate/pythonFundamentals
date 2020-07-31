def print_upper_words(words):
    """For a list of words, print out each word on a separate line, 
    but in all uppercase.
"""


# YOUR CODE HERE
    print(list(map(lambda x: x.upper(), words)))


# provided solution
def print_upper_words2(words):
    for word in words:
        print(word.upper())


def print_upper_words3(words):
    """Print each word on sep line, uppercased, if starts with E or e.

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words4(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print(print_upper_words4(["hello", "hey", "goodbye",
                          "yo", "yes"], must_start_with={"g"}))

print(print_upper_words4(["hello", "hey", "goodbye", "yo", "yes"],
                         must_start_with={"h", "y"}))
