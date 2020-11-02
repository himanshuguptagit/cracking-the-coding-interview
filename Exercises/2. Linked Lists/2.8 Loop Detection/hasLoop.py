import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def hasLoop(linkedList):
    
    isLoopPresent = False
    slow = linkedList.head
    fast = linkedList.head

    while(fast!= None or fast.next!=None):
        slow = slow.next
        fast = fast.next.next

        if(slow == fast):
            isLoopPresent = True
            break
    
    start = linkedList.head

    if isLoopPresent: 
        while(start != slow):
            start = start.next
            slow = slow.next
        return slow
    else: 
        return None



linkedList = LinkedList()
linkedList.appendNode(Node("A"))
linkedList.appendNode(Node("B"))
n1 = Node("C")
linkedList.appendNode(n1)
linkedList.appendNode(Node("D"))
linkedList.appendNode(Node("E"))
linkedList.appendNode(n1)

print("Input: ")
# linkedList.printList()
# do not print list since it contains a loop -> program will stuck in infinite loop
# A -> B -> C -> D -> E -> C

print("Output: ")
res = hasLoop(linkedList)
if res:
    print(f"Loop at: {res.data}")
else:
    print("Loop not detected.")



