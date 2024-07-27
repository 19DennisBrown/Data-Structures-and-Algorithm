

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def push(self, value):
    newNode = Node(value)
    if self.head:
      newNode.next  = self.head
    self.head = newNode
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "The stack is empty."
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value
  
  def peek(self):
    if self.isEmpty():
      return "The given stack is empty."
    return self.head.value
  
  def isEmpty(self):
    return self.size == 0
  
  def size(self):
    return self.size
  

thiStack = Stack()
  # creating stack
thiStack.push('A')
thiStack.push('B')
thiStack.push('C')

# operations
print(f"Popping : {thiStack.pop()}")
print(f"Peeking : {thiStack.peek()}")
# print(f"Size : {thiStack.size()}")
print(f"Empty? {thiStack.isEmpty()}")
