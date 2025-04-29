def arepairs(open,close):
    if open=='[' and close==']':
        return True
    elif open=='{' and close=='}':
        return True
    elif open=='(' and close==')':
        return True
    return False
def balance(equation):
    stack=[]
    for i in equation:
        if i in ['[', '{', '(']:
            stack.append(i)
        elif i in [']', '}', ')']:
            if len(stack)==0 or not arepairs(stack[-1],i):
                return False
            stack.pop()
    return len(stack)==0

A=["({a+b})","))((a+b}{","((a+b))", "))","[a+b]*(x+2y)*{gg+kk}"]
for equation in A:
    print(balance(equation))
