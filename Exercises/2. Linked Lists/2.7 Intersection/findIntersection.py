import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def findIntersection(l1, l2):
    
    len1 = l1.length()
    len2 = l2.length()
    diff= abs(len1 - len2)

    node1 = l1.head
    node2 = l2.head

    if(len1 > len2):
        for i in range(0,  diff):
            node1 = node1.next
    elif(len2 > len1):
        for i in range(0,  diff):
            node2 = node2.next

    while(node1 != None and node2 != None):
        if(node1 == node2):
            return node1
        
        node1 = node1.next
        node2 = node2.next
    return None





linkedList1 = LinkedList()
linkedList1.appendNode(Node(3))
linkedList1.appendNode(Node(1))
linkedList1.appendNode(Node(5))
linkedList1.appendNode(Node(9))

linkedList2 = LinkedList()
linkedList2.appendNode(Node(4))
linkedList2.appendNode(Node(6))

n1 = Node(7)
linkedList1.appendNode(n1)
linkedList2.appendNode(n1)

n2 = Node(2)
linkedList1.appendNode(n2)
linkedList2.appendNode(n2)

n3 = Node(1)
linkedList1.appendNode(n3)
linkedList2.appendNode(n3)

print("Input: ")
linkedList1.printList()
linkedList2.printList()

print("Output: ")
res = findIntersection(linkedList1, linkedList2)
if(res):
    print(f"intersection: {res.data}")
else:
    print(f"intersection not found")