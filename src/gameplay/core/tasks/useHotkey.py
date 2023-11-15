from src.utils.keyboard import send_key


def sendHotkey(hotkey, pycwnd):
    (modifier, hk) = parseHotkey(hotkey)
    send_key(hk, pycwnd, modifier=modifier)

def parseHotkey(hotkey):
    if "+" in hotkey:
        return hotkey.split("+")
    return (None, hotkey)
