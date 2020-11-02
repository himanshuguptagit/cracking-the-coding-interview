
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def printList(self):
        if(self.head==None):
            print("List is empty")
        node = self.head
        while(node!=None):
            if(node.next == None):
                print(node.data)
            else:
                print(node.data, end=" -> ")

            node = node.next
    
    def length(self):
        count = 0
        node = self.head
        while(node!=None):
            count += 1
            node = node.next
            
        return count

    def appendNode(self, node):
        if(self.tail):
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
    
    def push(self, node):
        if(self.head):
            node.next = self.head
        else:
            self.tail = node

        self.head = node


    def pop(self):
        res = None
        if(self.head):
            res = self.head.data
            self.head = self.head.next

        return res

    def popFromEnd(self):
        res = None

        if(self.head == None):
            res = None
        elif(self.head.next == None):
            res = self.head.data
            self.head = None
            self.tail = None
        else:
            node = self.head
            nextNode = node.next
            while(nextNode.next != None):
                node = nextNode
                nextNode = nextNode.next
            
            res = nextNode.data
            node.next = None
            self.tail = node
        
        return res

    


       
        
