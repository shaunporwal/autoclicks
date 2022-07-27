import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')

moving = False
mouse = Controller()

def _square_clickmove(radius=100):
    while True:
        if moving:
            mouse.click(Button.left, 1)
            time.sleep(0.001)
            mouse.click(Button.left, 1)
            mouse.move(0, -radius)
            time.sleep(0.5)
            mouse.move(radius, 0)
            time.sleep(0.5)
            mouse.move(radius, 0)
            time.sleep(0.5)
            mouse.move(0, radius)
            time.sleep(0.5)
            mouse.move(0, radius)
            time.sleep(0.5)
            mouse.move(-radius, 0)
            time.sleep(0.5)
            mouse.move(-radius, 0)
            time.sleep(0.5)
            mouse.move(0, -radius)
            time.sleep(0.5)
        time.sleep(0.001)

# def clicker():
#     while True:
#         if moving:
#             mouse.click(Button.left, 1)
#         time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global moving
        moving = not moving


_square_clickmove_thread = threading.Thread(target=_square_clickmove)

_square_clickmove_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
