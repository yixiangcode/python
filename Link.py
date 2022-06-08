import time
import schedule
print("上课Link助手")
def Time():
    theTime=time.localtime()
    if theTime[3]==13 and theTime[4]==20 and theTime[5]==0:
        print("现在是" , theTime[3] , ":" , theTime[4] , "的电脑课~")
        print("上课Link : " , "https://zoom.us/j/5906765099?pwd=bUNLT2RmcVpJbjJWbTEwbzFXZ3NZZz09")
    if theTime[3]==13 and theTime[4]==20 and theTime[5]==10:
        print("\n现在是" , theTime[3] , ":" , theTime[4] , "的电路课~")
        print("电路上课Link : " , "https://us04web.zoom.us/j/2468450244?pwd=M3QzTzJpYmhraytpbnNMRmZrU05hdz09")
    if theTime[3]==13 and theTime[4]==20 and theTime[5]==15:
        print("\n现在是" , theTime[3] , ":" , theTime[4] , "的数学课~")
        print("数学上课Link : " , "https://us04web.zoom.us/j/4645446141?pwd=VXlSbUxISGo2NG1DRldIRWg4MXNIdz09")
schedule.every(1).seconds.do(Time)
while True:
    schedule.run_pending()
    time.sleep(1)
