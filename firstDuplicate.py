# Given an array a that contains only numbers in the range from 1 to a.length, find
# the first duplicate number for which the second occurrence has the minimal index.
# In other words, if there are more than 1 duplicated numbers, return the number for
# which the second occurrence has a smaller index than the second occurrence of the other
# number does. If there are no such elements, return -1.

def solution(a):
    dict = {}
    key = 0

    for i in range(0, len(a)):

        key = a[i]
        if key in dict:
            dict[key] = dict[key] + 1

            if dict[key] == 2:
                return key
        else:
            dict[key] = 1

    return -1
