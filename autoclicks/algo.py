
import time
import threading
import pynput
from pynput.mouse import Controller as mouse, Button
from pynput.keyboard import Listener, KeyCode

# TOGGLE_CLICKER_KEY = KeyCode(char="t")
TOGGLE_MOVER_KEY = pynput.keyboard.KeyCode(char="m")
# clicking = False
moving = False
# mouse = Controller()


def _square_clickmove(radius: int = 100,
                      pausetime: float = 0.5
                      ):

    while True:
        if moving:
            mouse.click(Button.left, 1)
            time.sleep(0.001)
            mouse.click(Button.left, 1)
            mouse.move(0, -radius)
            time.sleep(pausetime)
            mouse.move(radius, 0)
            time.sleep(pausetime)
            mouse.move(radius, 0)
            time.sleep(pausetime)
            mouse.move(0, radius)
            time.sleep(pausetime)
            mouse.move(0, radius)
            time.sleep(pausetime)
            mouse.move(-radius, 0)
            time.sleep(pausetime)
            mouse.move(-radius, 0)
            time.sleep(pausetime)
            mouse.move(0, -radius)
            time.sleep(pausetime)


# def toggle_clicker(key):
#     if key == TOGGLE_CLICKER_KEY:
#         global clicking
#         clicking = not clicking


def run_clickmove(toggle_key: str = 'm',
                  radius: int = 100,
                  pausetime: float = 0.5
                  ):

    TOGGLE_MOVER_KEY = pynput.keyboard.KeyCode(char=toggle_key)

    # moving = False

    _square_clickmove(radius=radius,
                      pausetime=pausetime)

    mover_thread = threading.Thread(target=_square_clickmove(radius=radius,
                                                             pausetime=pausetime))

    mover_thread.start()

    def _toggle_mover(key):
        if key == TOGGLE_MOVER_KEY:
            global moving
            moving = not moving

    with Listener(on_press=_toggle_mover) as mover:
        mover.join()



run_clickmove()

