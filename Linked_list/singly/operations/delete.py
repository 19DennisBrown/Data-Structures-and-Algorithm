
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

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return  head.next
  currentNode  = head

  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next
  
  if currentNode.next is None:
    return head
  
  currentNode.next = currentNode.next.next

  return head

node1 = Node(70)
node2 = Node(71)
node3 = Node(72)
node4 = Node(73)  

node1.next = node2
node2.next = node3
node3.next = node4

print("Before deletion : ")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\n After deletion : ")
traverseAndPrint(node1)