
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

def deleteNode(head, targetNode):
  if head == targetNode:
    return head.next
  currentNode = head
  while currentNode.next and currentNode.next != targetNode:
    currentNode = currentNode.next
  if currentNode.next is None:
    return head
  currentNode.next = currentNode.next.next
  
  return head

node1 = Node(23)
node2 = Node(12)
node3 = Node(18)

node1.next = node2
node2.next = node3

print(f"Before deleting {node2}")
traverseAndPrint(node1)

print(f"\n After deleting {node2}")
# deleting
deleteNode(node1, node2)
traverseAndPrint(node1)