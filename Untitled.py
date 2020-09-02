class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, ele):
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
            if currentnode.next is None:
                print(currentnode.data)
                break
            print(currentnode.data)
            currentnode = currentnode.next
first_ele = Node("harith")
second_ele = Node("harshith")
third_ele = Node("shubha")
fourth_ele = Node("Marappa")

link = LinkedList()
link.append(first_ele)
link.append(second_ele)
link.append(third_ele)
link.append(fourth_ele)

link.printlist()
