# Note: Try to solve this task in O(n) time using O(1) additional space,
# where n is the number of elements in the list, since this is what you'll be asked to do during an interview.
#
# Given a singly linked list of integers l and an integer k, remove
# all elements from list l that have a value equal to k.

class LinkedNode(object):
    def __init__(self, x):
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
        
        if self.value == x:
            self = self.next
            
        node = self.next
        prev = self
        node.printList()
        prev.printList()
        
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
        print()

list = LinkedNode(1)
for i in range(2, 21):
    list.add(i)

list.remove(20)
list.printList()