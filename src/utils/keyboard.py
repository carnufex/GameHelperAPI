import os
import random
import time
import pyautogui

import win32con

import win32api
import win32gui
import win32service
import win32ui

pyautogui.PAUSE = 0

# Add alphanumeric keys
hotkey_dict = {}
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    hotkey_dict[char.lower()] = ord(char)

# Add special keys
special_keys = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'shift', 'control', 'space']
for key in special_keys:
    hotkey_dict[key] = getattr(win32con, 'VK_' + key.upper())

def send_keyboard_input(pycwnd, hotkey=None, msg=None, modifier=None):
    keys_to_send = []

    if modifier is not None:
        # keys_to_send.append(modifier.lower())
        pyautogui.keyDown(modifier)
        time.sleep(0.01)
    if hotkey is not None and hotkey.lower() in hotkey_dict:
        keys_to_send.append(hotkey.lower())

    for key in keys_to_send:
        pycwnd.SendMessage(win32con.WM_KEYDOWN, hotkey_dict[key], 0)

    if msg is not None:
        for c in msg:
            if c == "\n":
                pycwnd.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                pycwnd.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            else:
                pycwnd.SendMessage(win32con.WM_CHAR, ord(c), 0)

    for key in reversed(keys_to_send):
        pycwnd.SendMessage(win32con.WM_KEYUP, hotkey_dict[key], 0)

    if modifier is not None:
        # keys_to_send.append(modifier.lower())
        pyautogui.keyUp(modifier)

    pycwnd.UpdateWindow()

def send_key(hotkey, pycwnd, msg=None, modifier=None):
    send_keyboard_input(pycwnd, hotkey, msg, modifier)


def send_click_input(pycwnd, x, y, button='left', modifier=None):
    lParam = win32api.MAKELONG(x, y)

    # Move the mouse to the specified coordinates (optional but might be necessary)
    pycwnd.SendMessage(win32con.WM_MOUSEMOVE, 0, lParam)

    # Send modifier key down message if specified
    if modifier is not None and modifier.lower() in hotkey_dict:
        modifier_code = hotkey_dict[modifier.lower()]
        pycwnd.SendMessage(win32con.WM_KEYDOWN, modifier_code, 0)
        pycwnd.UpdateWindow()

    # Send mouse click messages
    if button == 'left':
        pycwnd.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        pycwnd.SendMessage(win32con.WM_LBUTTONUP, 0, lParam)
    elif button == 'right':
        pycwnd.SendMessage(win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        pycwnd.SendMessage(win32con.WM_RBUTTONUP, 0, lParam)
    else:
        raise ValueError("Invalid button type. Use 'left' or 'right'.")

    # Send modifier key up message if specified
    if modifier is not None:
        pycwnd.SendMessage(win32con.WM_KEYUP, modifier_code, 0)
        pycwnd.UpdateWindow()

def send_click(x, y, pycwnd, button='left', modifier=None):
    send_click_input(pycwnd, x, y, button, modifier)


