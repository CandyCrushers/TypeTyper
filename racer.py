from pyautogui import press, typewrite, hotkey
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pygetwindow as gw

time.sleep(3)

def is_google_docs_active():
    active_window = gw.getActiveWindow()
    if active_window:
        return "docs.google.com" in active_window.title
    return False 

try:
    if is_google_docs_active():
        print("Google Docs Detected!")
        time.sleep(2)
        press('a')
        typewrite("Hello world", interval=0.1)
        time.sleep(1)
        hotkey('ctrl', 'x')
    else:
        print("Not a google docs page!")
except Exception as e:
    print(f"An error occured: {e}")