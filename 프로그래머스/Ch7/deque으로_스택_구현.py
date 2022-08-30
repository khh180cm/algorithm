from collections import deque


stack = deque()

# push()
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)

print("Initial stack:")
print(stack)

# pop()
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after elements are popped:")
print(stack)
