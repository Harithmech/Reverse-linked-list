#creating a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

first_ele = Node(1)
lis = Linkedlist()
