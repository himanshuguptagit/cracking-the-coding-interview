import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def isPalindrome(linkedList):
    stack = LinkedList()
    res = True
    slow = linkedList.head
    fast = linkedList.head
    count=0

    while(fast!= None and fast.next !=None):
        count += 1
        stack.push(Node(slow.data))
        slow = slow.next
        fast = fast.next.next

    if(fast != None):
        slow = slow.next

    while(slow!= None):
        val1 = slow.data
        val2 = stack.pop()
        if(val1 != val2):
            res = False
            break
        slow = slow.next

    return res


linkedList = LinkedList()
linkedList.appendNode(Node(2))
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(4))
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(2))

print("Input: ")
linkedList.printList()

print("Output: ")
print(f"Palindrome: {isPalindrome(linkedList)}")


