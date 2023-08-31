
def p(x,y):
    p=x+y
    return p
def q(x,y):
    q=x-y
    return q
def r(x,y):
    r=x*y
    return r
def s(x,y):
    s=x/y
    return s

num1=eval(input("enter the first number : "))
num2=eval(input("enter the second number : "))
print("please select the operation. ")
print("a.Addition")
print("b.Substaction")
print("c.Multiplication")
print("d.Division")
choice=input("please enter the choice :(a,b,c,d) :\n")
if choice=='a':
    sum=p(num1,num2)
    print("Addition of",num1,"+",num2,"=",sum)
elif choice=='b':
    substaction=q(num1,num2)
    print("sustaction of",num1,"-",num2,"=",substaction)
elif choice=='c':
    multiplication=r(num1,num2)
    print("Multiplication of",num1,"*",num2,"=",multiplication)
elif choice=='d':
    division=s(num1,num2)
    print("Division of",num1,"/",num2,"=",division)
else:
    print("This is invalid input ")
    

