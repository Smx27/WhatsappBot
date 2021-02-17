import pyautogui,time
time.sleep(5)
for word in open("Script","r"):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
