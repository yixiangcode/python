import random
z=100
number=random.randint(0,z)
x=random.randint(0,z)
n=0
a=0
b=0
count=0
times=[]
frequency=int(input("你想要猜几次\n"))
while a < frequency:
    a+=1
    n=0
    number=random.randint(0,z)
    while x!=number:
        n+=1
        x=random.randint(0,z)
        if x==number:
            times.append(n)
for a in times:
    b+=1
    print("第",b,"次使用了",a,"次")
    print("---------------------------")
    count+=a
actual=len(times)
print("用了",count,"次完成了",actual,"次的猜数字任务")
y=float(count/actual)
print("平均用了",y,"求得答案")
deviation=z-y
print("误差值为",abs(deviation))
