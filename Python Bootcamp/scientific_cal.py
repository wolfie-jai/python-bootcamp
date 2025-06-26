def sccalc():
    d = 0
    a =  float(input("Enter first value  : "))
    print("Enter the operation you want to perform : ")
    print( "1 : Square")
    print( "2 : Square root")
    print( "3 : logarithm")
    c = input("Enter any arithmetic operation you want to perform : (1 , 2 , 3) : ")

    if (c == "1"):
        print('Square of num =' ,a**2)
    elif (c == "2"):
        print('Square root of num =' ,a**0.5)
    else :
        print("invalid input")

sccalc()
print(sccalc)