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
            return "Stack is not empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
def reverse(str):
    temstr=''
    stack=Stack()
    for i in range(len(str)):
        stack.push(str[i])
    while not stack.isEmpty():
        tem=stack.pop()
        temstr=temstr+tem
    return temstr
if __name__=="__main__":
    print(reverse("We will conquere COVID-19"))
