print("\n【第一题】\n")
A=[]
B=[]
开始, 结束 = 0, 100
for number in range(开始, 结束 + 1):
   if number % 2 != 0:
      A.append(number)
for number in range(开始, 结束 + 1):
   if number % 5 == 0:
      B.append(number)
A=set(A)
B=set(B)
print("A:",A)
print("B:",B)
print("A与B的交集：",A&B)
print("A与B的联集：",A|B)
print("A与B的差集：",A-B)
print("B与A的差集：",B-A)

print("\n【第二题】\n")
Math={"A","B","C","D","E","G","H","I"}
Computer={"B","D","G","W","X","Y","Z"}
Physics={"B","C","L","X","Z"}
print("Math:",Math)
print("Computer:",Computer)
print("Physics:",Physics)
print("同时参加3个生活营的名单：",Math&Computer&Physics)
print("同时参加Math和Computer生活营的名单：",Math&Computer)
print("同时参加Math和Physics生活营的名单：",Math&Physics)
print("同时参加Computer和Physics生活营的名单：",Computer&Physics)
