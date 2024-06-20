class Operations:
  def __init__(self, data):
    self.data = data
    self.next = None
def traverse(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
  print("null")
def lowestValue(head):
  minVal = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data  < minVal:
      minVal = currentNode.data
    currentNode = currentNode.data
  return minVal

node1 = Operations(3)
node2 = Operations(35)
node3 = Operations(333)
node4 = Operations(32)

node1.next = node2
node2.next = node3
node3.next = node4

# currentNode = node1

traverse(node1)
print(f"The lowest value is {lowestValue(node1)}")
