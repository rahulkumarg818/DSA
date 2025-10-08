class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.top
        self.top = newNode
        self.length += 1
        print(f"{val} Pushed to Stack")
        
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        popped_value = self.top.data
        self.top = self.top.next
        self.length -= 1
        print(f"Popped: {popped_value}")
        return popped_value

    def size(self):
        print(f"Stack size is {self.length}") 
    
    def getTop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print(f"Top is {self.top.data}")


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.getTop()
stack.size()
