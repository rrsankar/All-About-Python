# Node Attributes:
# 1. Value: Can be integers, string, object
# 2. The pointer to the next node

class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


# Let's make a linked list like the following.
# 3 -> 7 -> 10

node1 = LinkedListNode(value=3)
node2 = LinkedListNode(value=7)
node3 = LinkedListNode(value=10)

# We got three nodes that aren't connected.
# Now let's create connections between nodes.

node1.nextNode = node2  # 3 -> 7
node2.nextNode = node3  # 7 -> 10

# Now we have node1 -> node2 -> node3
# Lets test these connections by traversing from head.

currentNode = node1     # Setting node1 as head.
while True:
    print(f"{currentNode.value} -> ", end="")
    # Check if current node is tail node.
    if currentNode.nextNode is None:
        print("NULL")
        break
    else:
        currentNode = currentNode.nextNode
