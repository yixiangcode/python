data=[]
i=0
print("输入数据或输入 q或Q 以停止输入")
while i<100 :
    a=input()
    if a=="q" or a=="Q":
        break
    else:
        i+=1
        data.append(int(a))
def bubbleSort(x):
    s=1
    for i in range(len(x)-1):
        if s==1:
            s=0
            for j in range(len(x)-1-i):
                if x[j]<x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
                    s=1
            print("第",i+1,"轮",x)
        else:
            break
    return x
print(data)
print(bubbleSort(data))
