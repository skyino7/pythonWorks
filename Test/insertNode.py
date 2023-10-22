#!/usr/bin/python3

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must be a LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        tmp = self.head
        while (tmp):
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == "__main__":

    linkList = LinkedList()

    linkList.append(6)
    linkList.push(7)
    linkList.push(1)
    linkList.append(4)

    linkList.insertAfter(linkList.head.next, 8)

    print("Created Linked List: ", end=" ")
    linkList.printList()
