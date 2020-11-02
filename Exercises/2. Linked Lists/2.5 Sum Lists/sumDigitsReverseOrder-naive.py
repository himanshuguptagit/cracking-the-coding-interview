import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList

# (7-> 1 -> 6) => 617
def convertLinkedListToNumber(linkedList):
    sum, count = 0, 0
    node = linkedList.head
    while(node != None):
        sum += node.data*(10**count)
        node = node.next
        count += 1
    return sum
    

def sumDigitsReverseOrder(l1, l2):
    n1 = convertLinkedListToNumber(l1)
    n2 = convertLinkedListToNumber(l2)

    print(f"{n1} + {n2} =  {n1 + n2}")
    

linkedList1 = LinkedList()
linkedList1.appendNode(Node(7))
linkedList1.appendNode(Node(1))
linkedList1.appendNode(Node(6))

linkedList2 = LinkedList()
linkedList2.appendNode(Node(5))
linkedList2.appendNode(Node(9))
linkedList2.appendNode(Node(2))

print("Input: ")
linkedList1.printList()
linkedList2.printList()

print("Output: ")
sumDigitsReverseOrder(linkedList1, linkedList2)
