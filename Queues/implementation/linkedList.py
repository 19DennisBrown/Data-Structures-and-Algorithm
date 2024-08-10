
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(add, elem):
    new_node = Node(elem)
    if add.rear is None:
      add.front = add.rear = new_node
      add.length += 1
      return
    
    add.rear.next = new_node
    add.rear = new_node
    add.length += 1

  def dequeue(remove):
    if remove.empty():
      return "Queue is empty."
    temp = remove.front
    remove.front = temp.next
    remove.length -= 1
    if remove.rear is None:
      remove.front = None
    return temp.data
  
  def peek(top):
    if top.empty():
      return "Queue is empty."
    return top.front.data
  
  def empty(nothing):
    return nothing.length == 0
  
  def size(leni):
    return leni.length
  
  def printingQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end="-")
      temp = temp.next
    print()


myQueue = Queue()
temp = myQueue.enqueue(12)
myQueue.enqueue(19)
myQueue.enqueue(23)
myQueue.enqueue(45)

print("Queue: ", end="")
myQueue.printingQueue()

print(f"\n Size : {myQueue.size()}")
print(f"\n Top : {myQueue.peek()}")
print(f"\n Dequeue : {myQueue.dequeue()}")
