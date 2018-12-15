"""
While Loop
to generate odd numbers from 1 upto the number user specified
"""
i = 1
print("Enter the number : ")
n = int(input())
print("Odd numbers upto ",n)
while i < n:
    print(i)
    i += 2

# break and continue statements in while
print("When we use break :")
i = 0
while i < 10:
    i += 2
    if i == 6 :
        break     # it breaks the while loop
    print(i)

print("when we use continue :")
i = 0
while i < 10:
    i += 2
    if i == 6 :
        continue   #it skips the current iteration and starts next iteration
    print(i)

'''
OUTPUT:
Enter the number : 
10
Odd numbers upto  10
1
3
5
7
9
When we use break :
2
4
when we use continue :
2
4
8
10
'''
