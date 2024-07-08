# Node Attributes:
# 1. Value: Can be integers, string, object
# 2. The pointer to the next node
import copy


class LinkedlistNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


# Initially, the LinkedList is going to be empty.
# A node is created when we call the insert operation.
# The first node will be set as Head.

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """
        Function to insert a new node into LinkedList.
        If LL is empty set the new node as Head.
        If not empty, add as Tail node.
        """

        node = LinkedlistNode(value)

        # Let's check if the LL is empty. When it's first node in the LL.
        if self.head is None:
            self.head = node
            return

        # If LL is not empty.
        # Find the tail by traversing through the LL.
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def delete(self, input_value):

        currentNode = self.head
        previousNode = None

        while True:

            # Check if current node value is input value.
            if currentNode.value == input_value:

                if previousNode:

                    # Join previous node and next node.
                    previousNode.nextNode = currentNode.nextNode
                    print("Delete successful.")
                    return

                else:

                    # If there are no other nodes in LL.
                    if currentNode.nextNode is None:
                        self.head = None
                        print("Delete successful.")
                        return

                    # If there are other values in LL.
                    else:
                        self.head = currentNode.nextNode
                        print("Delete successful.")
                        return

            if currentNode.nextNode is None:
                print("Item not found.")
                break

            previousNode = currentNode
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(f"{currentNode.value} -> ", end="")
            currentNode = currentNode.nextNode
        print("NULL")


# LETS CREATE A LINKED LIST.
ll = LinkedList()
ll.insert(value=3)
ll.insert(value=7)
ll.insert(value=10)
ll.insert(value=30)
ll.printLinkedList()

# Delete a value.
ll.delete(input_value=30)
ll.printLinkedList()
