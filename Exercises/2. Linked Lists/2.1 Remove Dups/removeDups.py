import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Util.Node import Node
from Util.LinkedList import LinkedList


def deleteDups(head):
    dataSet = set()
    previous = head
    current = head.next
    dataSet.add(previous.data)
    while(current != None):

        if current.data in dataSet:
            previous.next = current.next

        else:
            dataSet.add(current.data)
            previous = current

        current = current.next

def deleteDupsWithoutBuffer(head):
    current = head

    while(current != None):
        runner = current
        while(runner!=None and runner.next != None):
            if(runner.next.data == current.data):
                runner.next = runner.next.next
            runner = runner.next
        current = current.next


linkedList = LinkedList()
linkedList.appendNode(Node(1))
linkedList.appendNode(Node(1))
linkedList.appendNode(Node(2))
linkedList.appendNode(Node(3))
linkedList.appendNode(Node(4))
linkedList.appendNode(Node(4))
linkedList.appendNode(Node(5))
linkedList.appendNode(Node(5))

print("Input: ")
linkedList.printList()

print("Output: ")
# deleteDups(linkedList.head)
deleteDupsWithoutBuffer(linkedList.head)
linkedList.printList()

