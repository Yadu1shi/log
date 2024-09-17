

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

def add():
    sum=a+b
    print("sum:",sum)
def sub():
    sum=a-b
    print("sub:",sum)
def mul():
    sum=a*b
    print("sum:",sum)
def div():
    sum=a/b
    print("sum:",sum)

operator = input("enter any simple operation from list of [+,-,*,/]:")

if operator=='+':
    add()
elif operator=='-':
    sub()
elif operator=='*':
    mul()
elif operator=='/':
    div()
else:
    print("Erorr: Andha h kya list nahi dikh rahi!")



