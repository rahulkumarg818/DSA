class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0

    def push(self,val):
        print(f"Pushed to Queue: {val}")
        newNode=Node(val)
        self.length+=1
        if self.front==None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    
    def pop(self):
        if self.front==None:
            self.rear=None
            print("Queue is Empty")
        else:
            self.length-=1
            popped=self.front.data
            self.front=self.front.next
            print(f"Popped element is {popped}")
    def size(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            print(f"Length of queue is {self.length}")
    
    def Front(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            print(f"Front is {self.front.data}")


q = Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.pop()
q.Front()
q.size()
