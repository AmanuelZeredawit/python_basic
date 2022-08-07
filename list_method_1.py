# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
# @ amanuel zeredawit August 05, 2022

def chop(lst):
    print(lst[1:-1])


def middle(lst):
    return lst[1:-1]
    pass
lst = [1,2,3,4]
chop(lst)
#m_list = middle(lst)
print(middle(lst))


