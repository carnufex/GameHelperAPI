import threading
import keyboard
import time

# Shared variable
lock = threading.Lock()

def key_listener(callback):
    while True:
        key = None

        
        # Check for specific key inputs
        if keyboard.is_pressed('page up'):
            key = 'pgup'
        elif keyboard.is_pressed('pgdn'):
            key = 'looting'
        elif keyboard.is_pressed('x'):
            key = 'looting'


        # Update the shared variable
        with lock:

            callback(key)


        # print(keyboard.read_event().name) # find key names

        time.sleep(0.1)  # Adjust the sleep duration as needed



