
import pyautogui
from src.utils.keyboard import send_click_input
from time import sleep


def pickUpLoot(pycwnd):
    pyautogui.keyDown('shift')
    for y in range(3):
        for x in range(3):
            send_click_input(pycwnd, 1050+x*100, 515+y*100, 'right')

    pyautogui.keyUp('shift')

    


