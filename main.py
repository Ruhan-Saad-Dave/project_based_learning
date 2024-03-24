num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

l1 = [num1, num2, num3]
n = len(l1)

for i in range(0, n-1):
    for j in range(i+1,n):
        if l1[i] > l1[j]:
            max = l1[i]
        elif l1[i] < l1[j]:
            max = li[j]

print(max)