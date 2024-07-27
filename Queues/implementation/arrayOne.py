

queue = []

# Enqueue
queue.append ('A')
queue.append('B')
queue.append('C')

print(f"This queue : {queue}")

# dequeue
element = queue.pop()
print(f"{queue} : removed element is {element}")

# peek
frontElement = queue[0]
print(f"In {queue}, the front element is {frontElement}")

# isEmpty
isEmpty = not bool(queue)
print(f"Is empty? {isEmpty}")

# size 
print(f"The size of the queue is {len(queue)}")

