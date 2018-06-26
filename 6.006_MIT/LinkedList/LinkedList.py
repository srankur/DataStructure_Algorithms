class LinkedListNode():
    def __init__(self,data):
        self.data = data
        self.next = None

    #def setNext(self,data):

    def printNode(self):
        print(self.data)



class LinkedList():

    def __init__(self):
        self.Head = None

        pass

    def AddNode(self, Node, ):
        if self.Head == None:
            self.Head = Node

        current = self.Head
        while current.next != None:
            current.next = Node
        return self.Head

    def RemoveNodeAtfront(self,data):
        pass

    def CountNode(self):
        pass

    def printList(self):
        pass




Node1 = LinkedListNode(20)
Node2 = LinkedListNode(30)
Node3 = LinkedListNode(40)

Node1.printNode()
Node2.printNode()
Node3.printNode()





