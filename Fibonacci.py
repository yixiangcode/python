y=[]
a=1
b=0
print(b)
print(a)
while a < 50000:
    c=b
    b=a
    a=c+b
    if a%2==0:
        y.append(a)
print(sum(y))
