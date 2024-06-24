class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def is_full(self):
        return len(self.elements) == self.capacity

    def push(self, value):
        if not self.is_full():
            self.elements.append(value)
        else:
            print("Stack is full!")

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            print("Stack is empty!")
            return None

    def top(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("Stack is empty!")
            return None


# Example usage
stack1 = Stack(capacity=5)
stack1.push(5)
stack1.push(2)
print(stack1.is_full())  
stack1.push(10)
stack1.push(7)
stack1.push(1)
print(stack1.is_full())  
print(stack1.top())     
print(stack1.pop())     
print(stack1.top())     
print(stack1.is_empty()) 
