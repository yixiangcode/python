import random
number = random.sample(range(1,43),7)
specialNumber = number.pop()
print("特别号码： %d" % specialNumber)
print("开奖号码： ", end="")
for num in sorted(number):
    print(num, end="   ")
print("")