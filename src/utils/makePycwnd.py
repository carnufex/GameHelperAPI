import ctypes
import win32gui
import win32ui

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        #if buff.value.find('Tibia - ') == -1:
        if buff.value.find('Tibia') == -1:
            pass
        else:
            titles.append(buff.value)
    return True

def find_tibia_title():
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    print(titles)
    return titles[0]

def get_whndl(title):
    whndl = win32gui.FindWindowEx(0, 0, None, title)
    return whndl

def make_pycwnd(hwnd):
    PyCWnd = win32ui.CreateWindowFromHandle(hwnd)
    return PyCWnd

def getPycwnd():
    title = find_tibia_title()
    whndl = get_whndl(title)
    return make_pycwnd(whndl)

