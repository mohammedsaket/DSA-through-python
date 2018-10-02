
class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    #size of Linked List

    def getSize(self):
        return self.size

    #insert a Node at Beginning

    def addNodeatbeg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        print(data,"Inserted at Beginning")

    # Delete (Beginning)

    def deleteNodeatbeg(self):
        ptr=self.head
        self.head=ptr.getNextNode()
        self.size-=1
        print((self.head).getData(),"Deleted (Starting) ")

    # Delete (Starting)

    def deleteNodeatend(self):
        ptr=self.head
        while (ptr.getNextNode()).getNextNode():
            ptr=ptr.getNextNode()
        ptr.setNextNode(None)
        self.size-=1
        print((self.head).getData(),"Deleted (Ending)")

    # to print Linked List

    def printNode(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.getNextNode()




myList = LinkedList()
print("Inserting")
myList.addNodeatbeg(5)
myList.addNodeatbeg(15)
myList.addNodeatbeg(25)
myList.addNodeatbeg(35)
myList.addNodeatbeg(45)
myList.addNodeatbeg(55)
print("Printing")
myList.printNode()
print("Size=",myList.getSize())
myList.deleteNodeatbeg()
myList.deleteNodeatbeg()
print("Printing")
myList.printNode()
print("Size=",myList.getSize())
myList.deleteNodeatend()
myList.deleteNodeatend()
print("Printing")
myList.printNode()
print("Size=",myList.getSize())
