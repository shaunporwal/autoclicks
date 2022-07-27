



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