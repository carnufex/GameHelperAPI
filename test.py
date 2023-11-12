import src.utils.core
from src.utils.makePycwnd import getPycwnd
from src.utils.keyboard import send_click

# grayScreenshot = src.utils.core.getScreenshot()
pycwnd = getPycwnd()
send_click(1045, 512, pycwnd, 'right')
#1045, 512