import pyautogui
import time
x=input("enter message")
y=int(input("how many times want to send message "))
print("open whatsapp and click on text box")
print("please wait")
time.sleep(5)
for range in (0,y):
  pyautogui.typewrite(x)
  pyautogui.press("enter")
