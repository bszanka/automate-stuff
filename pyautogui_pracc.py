import pyautogui

# Coordinates 0,0 is the top left corner of your monitor.
# In programming, increasing Y means going down and increasing X means going right.
# FAILSAFE EXIT: Move your mouse to the top left corner of your monitor in case of any infinite loops.

print(pyautogui.size())
pyautogui.moveTo(10, 10, duration=2)
pyautogui.moveRel(100, 0)
pyautogui.moveRel(-100, 0)
print(pyautogui.position())
# pyautogui.rightClick(10, 10)
print(pyautogui.KEYBOARD_KEYS)
# pyautogui.press('esc')
# pyautogui.hotkey('ctrl', 'c')


pyautogui.screenshot('screenshot.png')
# pyautogui.screenshot('/home/bszanka/Development/Projects/automate-stuff/screenshot.png')
# pyautogui.locateOnScreen('pathToImageThatNeedsToBeLocatedOnTheDisplay')
