# source: https://github.com/asweigart/pyautogui
# install: pip install pyautogui OR poetry add pyautogui 


import pyautogui
pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
# screenWidth, screenHeight = pyautogui.size()  # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position()  # Returns two integers, the x and y of the mouse cursor's current position.
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.click()  # Click the mouse at its current location.
# pyautogui.click(200, 220)  # Click the mouse at the x, y coordinates 200, 220.
# pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.doubleClick()  # Double click the mouse at the
# pyautogui.press('esc')  # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
