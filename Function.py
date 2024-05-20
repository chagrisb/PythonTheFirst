
import pyautogui as pyag
import time
def function_one():
    print("This is function one")

def close_window(window):
    window.destroy()

def findLocat():
    Width,Height = pyag.size()
    print(Width,Height)

def doubleClick():
    pyag.moveTo(900, 10)
    time.sleep(1)
    #pyag.doubleClick()
    #pyag.click()
    pyag.dragTo(-1979, 10, button='left',duration=1)