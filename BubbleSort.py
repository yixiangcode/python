showDebug=int(input("要查看最新六合彩号码排序过程吗？【1】是；【2】否："))
def bubbleSort(x):
    s=1
    for i in range(len(x)-1):
        print()
        if s==1:
            s=0
            for j in range(len(x)-1-i):
                if x[j]<x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
                    s=1
            if showDebug==1:
                print("第", i+1, "轮", x)
        else:
            break
    return x
def numberMaker(a,b,n):
    import random
    y=random.sample(range(a,b), n)
    return y
z=numberMaker(0, 42, 6)
print("六合彩号码：", z)
print("排序后结果：", bubbleSort(z))
