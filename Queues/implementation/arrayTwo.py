

class Kiu:
  # Initialize  empty queue
  def __init__(self):
    self.kiu = []
  # enqueue
  def addKiu(add, elem):
    add.kiu.append(elem)
  # dequeue
  def redusKiu(redus):
    if redus.isEmpty():
      return "Kiu is empty"
    return redus.kiu.pop(0)
  # first element
  def peek(fast):
    if fast.isEmpty():
      return "Queue is empty"
    return fast.kiu[0]
  # check if empty
  def isEmpty(empty):
    return len(empty.kiu) == 0
  # check size
  def kiuSize(size):
    return len(size.kiu)
# creating new queue
newKiu = Kiu()
# adding elements
elem1 = newKiu.addKiu('A')
elem1 = newKiu.addKiu('Aw')
elem1 = newKiu.addKiu('Ae')

newKiu.redusKiu()
print(f"First element in th queue is : {newKiu.peek()}")
print(f"The length of kiu is : {newKiu.kiuSize()}")