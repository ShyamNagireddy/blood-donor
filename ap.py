import pyautogui, time
time.sleep(10)
f = open("code.txt", "r")
for x in f:
    pyautogui.typewrite(x)