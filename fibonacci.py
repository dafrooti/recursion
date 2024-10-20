sum = 0

def recursion(n):
    global sum
    # for i in range(1, n+1):
    # sum = n+recursion(n-1)

    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        return recursion(n-1)+recursion(n-2)

n = int(input("Enter value: "))

print(recursion(n))