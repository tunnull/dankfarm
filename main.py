import time, pyautogui, os
if(os.name == 'nt'):
    osClearName == "cls"
    os.system('cls')
else:
    osClearName = 'clear'
    os.system('clear')

print("Starting in 3 seconds. Please focus Discord and select the text box.")
time.sleep(3)
print("Starting now, please leave your computer on and Discord open.")
if __name__ == '__main__':
    while True:
        pyautogui.write("/beg")
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("/dig")
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("/fish")
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("/hunt")
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        i=0
        while i<30:
            i += 1
            os.system(osClearName)
            print("Cycle completed, next cycle in: ",i)
            time.sleep(1)