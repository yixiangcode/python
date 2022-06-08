print("\n第一题\n")

x={}
y={}
#没有东西的时候会自动定义成dict所以我弄set
x=set()
y=set()
n=0

while n<100:
    n=n+1
    if (n%2)!=0:
        x.add(n)
print("在x超市打工的(第一个集合)有:",x,",其定义为",type(x))
n=0
while n<100:
    n=n+5
    y.add(n)

print("在y超市打工的(第二个集合)有:",y,",其定义为",type(y))
print("")
print("打两份工的数字(交集)有:",x&y)
print("有打工的数字(联集)有:",x|y)
print("只有在x超市打工的(差集x-y)有:",x-y)
print("只有在y超市打工的(差集y-x)有:",y-x)

print("\n第二题\n")

Math={"A","B","C","D","E","G","H","I"}
Computer={"B","D","G","W","X","Y","Z"}
Physics={"B","C","L","X","Z"}
print("三个生活营都参加的有钱佬有",Math&Computer&Physics)
print("有参加数学和电脑营的是",Math&Computer)
print("有参加数学和物理营的是",Math&Physics)
print("有参加电脑和物理营的是",Computer&Physics)
