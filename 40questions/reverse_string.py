def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_phrase = phrase[::-1] 
    return new_phrase

print(reverse_string('Hola'))
print(reverse_string('awesome'))
print(reverse_string('sauce'))


#------------------------------------------
# school solution

#     return phrase[::-1]
