def fib(n):
    if(n<0):
        print("invalid number")

    elif(n==0):
              return 0
    elif(n==1):
              return 1
    else:
              return(fib(n-1)+fib(n-2))


ele=int(input("enter the number"))
for i in range(0,ele):
               print(fib(i))
