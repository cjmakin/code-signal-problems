# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def solution(l):
    
    if l == None:
        return True
       
    p = l
    arr = []
    
    while p:
        arr.append(p.value)
        p = p.next
        
    i = 0
    j = len(arr) - 1
    
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    
    return True