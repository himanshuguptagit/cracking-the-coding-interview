import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def kthToLast(head, k):
    currentNode = head
    referenceNode = head
    for i in range(1,k):
        referenceNode = referenceNode.next

    while(referenceNode!=None and referenceNode.next!=None):
        referenceNode = referenceNode.next
        currentNode = currentNode.next
    
    return currentNode.data




linkedList = LinkedList()
linkedList.appendNode(Node(1))
linkedList.appendNode(Node(2))
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(4))
linkedList.appendNode(Node(5))
linkedList.appendNode(Node(6))

print("Input: ")
linkedList.printList()

print("Output: ")

# deleteDups(linkedList.head)
print(f"1st from last: {kthToLast(linkedList.head, 1)}")
print(f"2nd from last: {kthToLast(linkedList.head, 2)}")
print(f"3rd from last: {kthToLast(linkedList.head, 3)}")
print(f"6th from last: {kthToLast(linkedList.head, 6)}")

