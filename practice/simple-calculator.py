def calcu():
    a = float(input("Enter first value  : "))
    b = float(input("Enter second value : "))
    c = input("Enter any arithmetic operation you want to perform : (+ , - , * , /) : ")
    if (c == "+"):
     print(a , "+" , b , '=' ,a+b)
    elif (c == "-"):
        print(a , "-" , b , '=' ,a-b)
    elif (c == "*"):
        print(a , "*" , b , '=' ,a*b)
    elif (c == "/"):
        if (b == 0):
            print('Second num cant be zero')
        else:
            print(a, "/" , b , '=' ,a/b)
    else :
        print('User inserted wrong values or operation')

while (0<1):
    calcu()
    print(calcu)

