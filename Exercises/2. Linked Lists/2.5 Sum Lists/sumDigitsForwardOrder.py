import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


# def addDigits(result, node1, node2):
#     carry = 0
#     if(node1.next and node2.next):
#         carry = addDigits(result, node1, node2)
#     elif(node1.next and not node2.next):
    

#     val1 = node1.data if node1 else 0
#     val2 = node2.data if node2 else 0
#     sum = val1 + val2 + carry
#     result.appendNode(Node(sum%10))
#     carry = sum // 10
#     return carry

def padListWithZero(linkedList, count):
    while(count>0):
        linkedList.push(Node(0))
        count -= 1

def addDigits(l1, l2):
    result, carry = None, 0

    if(l1.next or l2.next):
        result , carry = addDigits(l1.next,l2.next)

    if(not result):
        result = LinkedList()

    sum = l1.data + l2.data + carry
    print(f"{l1.data} + {l2.data} + {carry} = {sum}")

    result.push(Node(sum%10))
    carry = sum // 10

    return result, carry


def sumDigitsForwardOrder(linkedList1, linkedList2):
    len1 =linkedList1.length()
    len2 = linkedList2.length()
    higherLength = 0

    if(len1 > len2):
        padListWithZero(linkedList2, len1-len2)
        higherLength = len1
    elif(len2 > len1):
        padListWithZero(linkedList1, len2-len1)
        higherLength = len2
  
    result, carry = addDigits(linkedList1.head, linkedList2.head)
    if(carry):
        result.push(Node(carry))
    return result
    
    


linkedList1 = LinkedList()
# 617
linkedList1.appendNode(Node(6))
linkedList1.appendNode(Node(1))
linkedList1.appendNode(Node(7))

# 9864
linkedList2 = LinkedList()
linkedList2.appendNode(Node(9))
linkedList2.appendNode(Node(8))
linkedList2.appendNode(Node(6))
linkedList2.appendNode(Node(4))

print("Input: ")
linkedList1.printList()
linkedList2.printList()

print("Output: ")
res = sumDigitsForwardOrder(linkedList1, linkedList2)
res.printList()
