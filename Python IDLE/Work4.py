list = range(32,78953)
oddlist = [num for num in list if num % 2 == 1]
evenlist = [num for num in list if num % 2 == 0]
oddprimelist = [num for num in oddlist if num > 1 and len([i for i in range(2, num) if num % i == 0]) == 0]
print(oddlist)
print(evenlist)
print(oddprimelist)
