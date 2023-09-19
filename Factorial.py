def factorial(n):
    if n==1 or n==0:
        return 1
    if n<0:
        return "Rethink the problem, please."
    for i in range (1,n):
        n=n*i
    return n

x = int(input("So you want to calculate the factorial of "))
print(factorial(x))
     



