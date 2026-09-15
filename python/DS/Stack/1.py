stack = []

# push 
stack.append(10)
stack.append(20)
stack.append(30)


print(stack)

# pop
stack.pop()
print(stack)

# peek -> top element
print(stack[-1])


# check stack empty
print(len(stack) == 0)