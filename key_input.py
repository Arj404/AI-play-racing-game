from pynput import keyboard
import time
time.sleep(3)
keyboard = keyboard.Controller()

def press_a():
	keyboard.press('a')
	keyboard.release('a')
def press_d():
	keyboard.press('d')
	keyboard.release('d')
def press_s():
	keyboard.press('s')
	keyboard.release('s')
def press_w():
	keyboard.press('w')
	keyboard.release('w')

# press_a()
# press_d()
# press_s()
# press_w()