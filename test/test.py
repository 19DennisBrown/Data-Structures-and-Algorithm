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