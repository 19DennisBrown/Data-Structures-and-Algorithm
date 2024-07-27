
class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, element):
    return self.stack.append(element)
  
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]
  
  def isEmpty(self):
    return len(self.stack) == 0
  
  def size(self):
    return len(self.stack)
  
  # creating stack
thiStack = Stack()
thiStack.push('A')
thiStack.push('B')
thiStack.push('C')

print(f"Content : {thiStack.stack}")
print(f"Popping : {thiStack.pop()}")
print(f"Peeking : {thiStack.peek()}")
print(f"Size : {thiStack.size()}")
print(f"Empty? {thiStack.isEmpty()}")