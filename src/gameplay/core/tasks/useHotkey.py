from src.utils.keyboard import send_key
from .common.base import BaseTask
import time



class UseHotkeyTask(BaseTask):
    def __init__(self, hotkey: str, pycwnd: str, delayAfterComplete: int = 0.1):
        super().__init__()
        self.name = 'useHotkey'
        self.delayAfterComplete = delayAfterComplete
        self.hotkey = hotkey
        self.pycwnd = pycwnd

    # TODO: add unit tests
    def do(self, context):
        (modifier, hk) = self.parseHotkey(self.hotkey)
        send_key(hk, self.pycwnd, modifier=modifier)
        return context
    
    def parseHotkey(self, hotkey):
        if "+" in hotkey:
            return hotkey.split("+")
        return (None, hotkey)
