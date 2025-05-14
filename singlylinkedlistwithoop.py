

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insertAtTheEnd(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def deleteFromEnd(self):
        if self.head is None:
            return "Linked List is empty"
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deletefromBegining(self):
        if self.head is None:
            return "Linked List is empty"

        self.head = self.head.next





    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtBeginning("fox")
    llist.insertAtBeginning("brown")
    llist.insertAtBeginning("quick")
    llist.insertAtBeginning("the")
    llist.printLinkedList()
    llist.insertAtTheEnd("jumps")
    llist.printLinkedList()

    llist.deleteFromEnd()
    llist.printLinkedList()

    llist.deletefromBegining()
    llist.printLinkedList()


