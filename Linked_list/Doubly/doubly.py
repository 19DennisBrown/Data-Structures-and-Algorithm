"""
 ?Doubly linked list

  Has nodes to the both the previous and next node. Takes more memory. They are useful if one wants to move both down and up the list.
"""

class DoublyNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

firstNode = DoublyNode(3)
secondNode = DoublyNode(5)
thirdNode = DoublyNode(50)
fourthNode = DoublyNode(30)

# first node
firstNode.next = secondNode
# second node
secondNode.prev  = firstNode
secondNode.next = thirdNode
# third node
thirdNode.prev = secondNode
thirdNode.next = fourthNode
# fourth node
fourthNode.prev = thirdNode

print("\n While traversing forward")
thisNode = firstNode
while thisNode:
  print(thisNode.data , end="->")
  thisNode = thisNode.next
print("null")

print("\n While traversing backward")
thisNode = fourthNode
while thisNode:
  print(thisNode.data, end="->")
  thisNode = thisNode.prev
print("null")