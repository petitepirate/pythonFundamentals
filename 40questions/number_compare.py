def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        return 'Numbers are equal'
    elif a > b:
        return 'First number is greater'
    elif a < b:
        return 'Second number is greater'
    else:
        return 'Invalid' #will never run since invalid char throw errors

print(number_compare(2,3))
print(number_compare(4,3))
print(number_compare(4,4))

#---------------------------------------------------
# School Solution 

#     if a > b:
#         return "First is greater"
#     elif b > a:
#         return "Second is greater"
#     else:
#         return "Numbers are equal"
