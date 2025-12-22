# for i in range(1, 10):
#     print(i)

# def rec(n):
#     #base
#     if n > 10:
#         return
    
#     print(n)
#     #pre procsss
#     rec(n + 1)

#     return 

#Fibonacci numbers
def Fibo(n):
    #base case
    if n <= 1:
        return n
    
    #the process
    oneBack = Fibo(n - 1)
    twoBack = Fibo(n - 2)

    return oneBack + twoBack

print(Fibo(7))

