
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
  print(f"null")

def addNew(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode
  currentNode = head

  for _ in range(position-2):
    if currentNode is None:
      break
    currentNode = currentNode.next
  
  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(5)
node2 = Node(6)

node1.next = node2

# Legacy list
print(f"Legacy list")
traverseAndPrint(node1)

# Adding new node
node3 = Node(43)
posn = 3
node1 = addNew(node1, node3, posn)

# Updated list
print(f"Updated list")
traverseAndPrint(node1)