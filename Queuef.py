class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    def isEmpty(self):
        return self.queue==0
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
myQ=Queue()
print("The queue is:")
myQ.enqueue("A")
myQ.enqueue("B")
myQ.enqueue("C")
myQ.enqueue("D")
myQ.enqueue("E")
print(myQ.queue)

print("The element that is removed from teh queue is:",myQ.dequeue())
print("Peek element is:",myQ.peek())
print("Check if the element is empty:",myQ.isEmpty())
print("Size of the Queue:",myQ.size())
