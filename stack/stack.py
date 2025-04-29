class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)


if __name__=="__main__":
    myStack=Stack()
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    myStack.push(60)
    myStack.push(70)
    print(myStack.pop())
    print(myStack.stack)
