def recursion(base, expo):
    # global base, expo
    # for i in range(1, n+1):
    # sum = n+recursion(n-1)

    if expo==0:
        return 1
    elif expo==1:
        return base
    else: 
        return base*recursion(base, expo-1)

base = int(input("Enter base value: "))
expo = int(input("Enter exponential value: "))

print(recursion(base, expo))