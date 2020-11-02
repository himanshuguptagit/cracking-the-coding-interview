import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def deleteMiddleNode(node):
    if(node == None or node.next == None):
        return False
        
    node.data = node.next.data
    node.next = node.next.next
    return True

linkedList = LinkedList()
linkedList.appendNode(Node(1))
testNode = Node(2)
linkedList.appendNode(testNode)
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(4))
linkedList.appendNode(Node(5))

print("Input: ")
linkedList.printList()

print("Output: ")

# deleteDups(linkedList.head)
deleteMiddleNode(testNode)
linkedList.printList()
