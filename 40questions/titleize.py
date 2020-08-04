def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    return phrase.title()


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
# --------------school solution same as mine
# or, if you didn't know that, could capitalize each word by hand
# return ' '.join([s.capitalize() for s in phrase.split(' ')])
