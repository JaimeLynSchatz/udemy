# mouse control

import pyautogui

width, height = pyautogui.size()

pyautogui.position()

 pyautogui.click(45, 1683)
>>> pyautogui.click(45, 1683)
>>> def pausevid():
...   pyautogui.click(45, 1683)
...   pyautogui.moveTo(2171, 1683)
...
>>> pausevid()
>>> def ps():
...   pyautogui.click(45, 1683)
...   pyautogui.click(2171, 1683)
...
>>> ps()
>>> ps()

# pyautogui has a FAILSAFE -- move the mouse quickly to the 0,0 upper left hand corner

# use pyautogui.displayMousePosition() when running in interactive editor
