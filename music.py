#creating a linked list
#adding elements to linke list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertend(self, ele):
        if self.head is None:
            self.head = ele
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next
            lastnode.next = ele

    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            else:
                print(currentnode.data)
                currentnode = currentnode.next

first_ele = Node(1)
second_ele = Node(2)
third_ele = Node(3)
lis = Linkedlist()
lis.insertend(first_ele)
lis.insertend(second_ele)
lis.insertend(third_ele)
lis.printlist()