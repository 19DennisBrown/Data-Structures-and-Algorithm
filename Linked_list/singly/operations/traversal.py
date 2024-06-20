
"""
  Traversing  a linked list means to go through the linked list by following the links from one node to the next.
  It is typically done to search for specific node, and read or modify the node's content, remove the node or insert  a node right after or before that node.
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
  print("null")

def findTheLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.data
  return minValue

node1 = Node(4)
node2 = Node(0)
node3 = Node(11)

node1.next = node2
node2.next = node3

currentNode = node1

traverseAndPrint(node1)
print(findTheLowestValue(currentNode))