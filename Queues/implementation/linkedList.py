

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, element):
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return 
    
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1

    if self.front is None:
      self.rear = None
    return temp.data
  
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.front.data
  
  def isEmpty(self):
    return self.length == 0
  
  def size(self):
    return self.length
  
  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" ")
      temp = temp.next
    print()


thisQueue = Queue()

thisQueue.enqueue('A')
thisQueue.enqueue('B')
thisQueue.enqueue('C')

print("Queue: ", end="")
thisQueue.printQueue()

print("Dequeue: ", thisQueue.dequeue())
print("Peek: ", thisQueue.peek())
print("Is Empty? : ", thisQueue.isEmpty())
print("Size : ", thisQueue.size())


      