

"""
  ?Circular linked list
    It is like the singly or doubly linked list with the first node, the 'head', and the last node , the 'tail', connected.
    They are good for lists you need to cycle through continously.
    ?Types{
      1. singly linked list
      2. doubly linked list
    }
"""

# circular linked list
class SinglyNode:
  def __init__(self, data):
    self.data  = data
    self.next = None

firstNode = SinglyNode(2)
secondNode = SinglyNode(3)
thirdNode = SinglyNode(7)
fourthNode = SinglyNode(6)

firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = firstNode

thisNode = firstNode
startNode = firstNode

print(thisNode.data, end="->")
thisNode = thisNode.next

while thisNode != startNode:
  print(thisNode.data, end="->")
  thisNode = thisNode.next
print("...")


# doubly linked list

class DoublyNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

# first node
firstNode.prev = fourthNode
firstNode.next = secondNode
# second node
secondNode.prev = firstNode
secondNode.next = thirdNode
# third node
thirdNode.prev = secondNode
thirdNode.next = fourthNode
# fourth node
fourthNode.prev = thirdNode
fourthNode.next = firstNode


# forward traversal
print("\n  While traversing forward")
thisNode = firstNode
startNode = firstNode
print(thisNode.data, end="->")
thisNode = thisNode.next

while thisNode != startNode:
  print(thisNode.data, end="->")
  thisNode = thisNode.next
print("...")
# backward traversal
print("\n While traversing backward")
thisNode = fourthNode
startNode = fourthNode
print(thisNode.data, end="->")
thisNode = thisNode.prev

while thisNode != startNode:
  print(thisNode.data, end="->")
  thisNode = thisNode.prev
print("...")