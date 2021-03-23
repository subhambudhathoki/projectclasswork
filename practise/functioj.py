#defining function
def sum():
    print("inside the function")
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    answer=num1 + num2
    print(f'the sum of{num1} and {num2} is{answer}')
def sub():
    num1=int(input("first number"))
    num2=int(input("Second number"))
    subt=num1 - num2
    print(f"the answer after substracting num1 from num2 is {subt}")
def mul():
    num1=int(input("first number"))
    num2=int(input("Second number"))
    mult=num1 * num2
    print(f"the answer after multplying num1 from num2 is {mult}")
print("calling function")
sum()
print("program is over")
print("second call")
sub()
print("third call")
mul()






