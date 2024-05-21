
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
    pyag.doubleClick()

def dragANDdrop():
    pyag.moveTo(900, 10)
    time.sleep(1)
    pyag.dragTo(-1979, 10, button='left',duration=1)

def printtest():
    # อ่านข้อมูลจากไฟล์ credentials.txt
    with open('credentials.txt', 'r') as file:
        ids = file.read().splitlines()

    # สร้าง object (list of dictionaries) จากข้อมูลในไฟล์
    credentials = []
    for index, id in enumerate(ids):
        if (index + 1) == 5:
            password = "123456"
        else:
            password = "password"
        credentials.append({"ID": id, "Password": password})

    # วนลูปปรินข้อความจาก object
    for cred in credentials:
        print(f"ID: {cred['ID']}, Password: {cred['Password']}")