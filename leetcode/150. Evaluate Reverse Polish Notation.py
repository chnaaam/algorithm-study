tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
operations = "+*-/"
num_stack = []

for t in tokens:
    if t in operations:
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        
        if t == "+":
            num_stack.append(num1 + num2)
        elif t == "*":
            num_stack.append(num1 * num2)
        elif t == "-":
            num_stack.append(num1 - num2)
        else:
            num_stack.append(int(num2 / num1))
    else:
        num_stack.append(int(t))
    
print(num_stack)