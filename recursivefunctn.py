"""Recursive function to generate fibonacci series"""
def recursive_fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(recursive_fib(n-1) + recursive_fib(n-2))
 
print("Enter the number of terms : ")
n=int(input())
print("Fibonacci series is given by: ")
"""Recursive function to print
     fibonacci series upto n terms"""
for i in range(n):
    print(recursive_fib(i))
"""n terms will be printed"""



'''
OUTPUT:
Enter the number of terms : 
10
Fibonacci series is given by: 
0
1
1
2
3
5
8
13
21
34
'''
