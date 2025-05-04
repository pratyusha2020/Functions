def add(P,Q):
    return P+Q

def sub(P,Q):
    return P-Q

def multiply(P,Q):
    return P*Q

def div(P,Q):
    return P/Q

print("Please select an operator")
print("a:Add")
print("b: Substract")
print("c: Multiply")
print("d: Divide")

choice= input("Enter choice a/b/c/d")

if choice== "a":
    num_1= int(input("Enter your first number"))
    num_2= int(input("Enter your second number"))
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif choice== "b":
    num_1= int(input("Enter your first number"))
    num_2= int(input("Enter your second number"))
    print(num_1, "-", num_2, "=", sub(num_1,num_2))
elif choice== "c":
    num_1= int(input("Enter your first number"))
    num_2= int(input("Enter your second number"))
    print(num_1, "x", num_2, "=", multiply(num_1,num_2))
elif choice== "d":
    num_1= int(input("Enter your first number"))
    num_2= int(input("Enter your second number"))
    print(num_1, "/", num_2, "=", div(num_1,num_2))

else: 
    print("Invalid input")