#import os
import pyautogui as g
import time
import schedule
#time.sleep(3)
#print(g.position())
#pyautogui.hotkey('ctrl','esc')
def Meet():
    chrome=g.locateOnScreen('Chrome.jpg',grayscale=True,confidence=.5)
    g.moveTo(chrome)
    g.typewrite('meet.google.com')
    g.press('enter')
Meet()
#g.typewrite('meet.google.com',interval=1)
#pyautogui.screenshot('screen.png')
#print(pyautogui.size())
#os.startfile(r'C:\Users\user\OneDrive\桌面\Test.txt')
