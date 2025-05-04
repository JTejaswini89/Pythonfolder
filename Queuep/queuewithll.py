lass Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    def enqueue(self,element):
        node=Node(element)
        if self.front is None:
            self.front=self.rear=node
            self.length+=1
            return
        self.rear.next=node
        self.rear=node
        self.length+=1
    def print_q(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        temp=self.front#front value is assigned to the variable temp
        self.front=temp.next#now temp is the front value and teh next value to temp is self.front
        self.length-=1
        if self.front is None:
            self.rear=None
        return temp.data
    def peek(self):
        return self.front.data
    def isEmpty(self):
        return self.length==0
    def size(self):
        return self.length
        
myQ=Queue()
myQ.enqueue(10)
myQ.enqueue(20)
myQ.enqueue(30)
myQ.print_q()
myQ.dequeue()
myQ.print_q()
print("The peek element from the queue is:",myQ.peek())
print("Is the queue empty:",myQ.isEmpty())
print("The length of the Queue:",myQ.size())
        
