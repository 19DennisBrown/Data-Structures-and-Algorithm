
stack = []

# push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print(f"Stack : {stack}")

# pop
element = stack.pop()
print(f"Stack : {stack}, {element} is deleted.")

# peek: what is the top element of the stack?
topElement = stack[-1]
print(f"{topElement} is the top element")

# Checking if is empty: isEmpty
isEmpty = not bool(stack)
print(f"{isEmpty}")

# size 
print(f"The stack size is {len(stack)}")