import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def partition(linkedList, x):
    previous = linkedList.head
    current = linkedList.head.next
    while(current != None):
        if(current.data < x):
            previous.next = current.next
            temp = current #can avoid creating temp variable but it makes it simpler to understand
            temp.next = linkedList.head
            linkedList.head = temp
            current = previous.next
        else:
            previous = previous.next
            current = current.next

    

linkedList = LinkedList()
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(5))
linkedList.appendNode(Node(8))
linkedList.appendNode(Node(5))
linkedList.appendNode(Node(10))
linkedList.appendNode(Node(2))
linkedList.appendNode(Node(1))
x = 5

print("Input: ")
linkedList.printList()
print(f"x: {x}")

print("Output: ")

# deleteDups(linkedList.head)
partition(linkedList, x)
linkedList.printList()
