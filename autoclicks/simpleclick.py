import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')

clicking = False
moving = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

####
def toggle_event(key):
    if key == TOGGLE_KEY:
        global moving
        moving = not moving

_square_clickmove_thread = threading.Thread(target=_square_clickmove)
_square_clickmove_thread.start()
####

with Listener(on_press=toggle_event) as listener:
    listener.join()
