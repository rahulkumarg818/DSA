class Stack:

    def __init__(self):
        self.stack=[]

    def show(self):
        print(self.stack) 
    
    def push(self,val):
        self.stack.append(val)
        print(f"{val} Pushed to stack")
    
    def pop(self):
        if self.stack==[]:
            return "Stack is Empty"
        else:
            return self.stack.pop()
    
    def top(self):
        if self.stack==[]:
            return "Stack is Empty"
        else:
            print("Top Element :" ,self.stack[-1])
        
    def size(self):
        print(f"Size of stack : {len(self.stack)}") 


stak=Stack()
stak.push(10)
stak.push(20)
stak.push(30)
stak.push(40)
stak.push(50)

stak.top()
stak.size()