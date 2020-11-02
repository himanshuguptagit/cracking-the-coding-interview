import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList

    
def sumDigitsReverseOrder(l1, l2):
    node1 = l1.head
    node2 = l2.head
    count, carry = 0, 0
    result = LinkedList()
    while(not (node1 == None and node2 == None)):
        val1 = node1.data if node1 else 0
        val2 = node2.data if node2 else 0
        sum = val1 + val2 + carry
        result.appendNode(Node(sum%10))
        carry = sum // 10

        if(node1):
            node1 = node1.next
        if(node2):
            node2 = node2.next
  
    if(carry):
        result.appendNode(Node(carry))

    return result

linkedList1 = LinkedList()
# 617
linkedList1.appendNode(Node(7))
linkedList1.appendNode(Node(1))
linkedList1.appendNode(Node(6))

# 9995
linkedList2 = LinkedList()
linkedList2.appendNode(Node(5))
linkedList2.appendNode(Node(9))
linkedList2.appendNode(Node(9))
linkedList2.appendNode(Node(9))

print("Input: ")
linkedList1.printList()
linkedList2.printList()

print("Output: ")
res = sumDigitsReverseOrder(linkedList1, linkedList2)
res.printList()
