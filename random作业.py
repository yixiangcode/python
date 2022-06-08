import random
magnum = random.sample( range(1, 50), 7 )
specialnum=magnum.pop()
print("第一期EE万能开奖号码 ", end = "")
for num in sorted( magnum ):
    print( num, end = " ")
print( "\n特别号码：%d"%specialnum )
