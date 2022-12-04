# Note: Try to solve this task in O(n) time using O(1) additional space, 
# where n is the number of elements in the list, since this is what you'll be asked to do during an interview.
# 
# Given a singly linked list of integers l and an integer k, remove 
# all elements from list l that have a value equal to k.

class LinkedNode(object):
    def __init__(self, x) :
        self.value = x
        self.next = None

    def add(self, x):
        newNode = LinkedNode(x)
        node = self
        while node:
            if node.next == None:
                node.next = newNode
                break
            node = node.next

    def remove(self, x):
        node = self.next
        prev = self

        if self.value == x:
            self = node.next
            
        else:

            while node:
                if node.value == x:
                    prev.next = node.next
                prev = node
                node = node.next
            


    def printList(self):
        node = self
        while node:
            print(node.value, end=" ")
            node = node.next

    
        


list = LinkedNode(1)
for i in range(2, 20):
    list.add(i)

list.printList()
list.remove(1)
print()
list.printList()


    