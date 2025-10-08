class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1

    def show(self):
        if self.front == -1 or self.front >= len(self.queue):
            print("Queue is Empty")
        else:
            print("Queue:", self.queue[self.front:]) 
    
    def push(self, val):
        if self.front == -1:
            self.front = 0
        self.queue.append(val)
        print(f"{val} Pushed to Queue")
    
    def pop(self):
        if self.front == -1 or self.front >= len(self.queue):
            print("Queue is Empty")
        else:
            popped = self.queue[self.front]
            self.front += 1
            print(f"{popped} is Popped Out")
            if self.front == len(self.queue):
                self.front = -1
                self.queue.clear()
            return popped
    
    def Front(self):
        if self.front == -1 or self.front >= len(self.queue):
            print("Queue is Empty")
        else:
            print("Front Element:", self.queue[self.front])
        
    def size(self):
        if self.front == -1 or self.front >= len(self.queue):
            print("Queue is Empty")
        else:
            print(f"Size of Queue: {len(self.queue) - self.front}") 


# Example usage
queu = Queue()
queu.push(10)
queu.push(20)
queu.push(30)
queu.push(40)
queu.push(50)
queu.pop()
queu.Front()
queu.size()
queu.show()
