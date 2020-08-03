def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    if lst == []:
        return 'none'
    else:
        return lst[-1]

print(last_element([2,3,4]))

#--------------------------------------------------------------

# Schools solution
#     if lst:
#         return lst[-1]

#     # we don't need to do anything else; functions
#     # return None by default
