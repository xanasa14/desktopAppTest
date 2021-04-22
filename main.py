import pyautogui, time

pauseSeconds = 0.3

# Open Windows Calculator via CLI
pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('calc', )
pyautogui.press('enter', )

# Wait for the Calculator: 2 Seconds
time.sleep(2)

# Addition
pyautogui.press('escape', _pause=pauseSeconds)
pyautogui.press('7', _pause=pauseSeconds)
pyautogui.press('+', _pause=pauseSeconds)
pyautogui.press('3', _pause=pauseSeconds)
pyautogui.press('enter', _pause=pauseSeconds)

# Subtraction
pyautogui.press('escape', _pause=pauseSeconds)
pyautogui.press('7', _pause=pauseSeconds)
pyautogui.press('-', _pause=pauseSeconds)
pyautogui.press('3', _pause=pauseSeconds)
pyautogui.press('enter', _pause=pauseSeconds)

# Multiplication
pyautogui.press('escape', _pause=pauseSeconds)
pyautogui.press('7', _pause=pauseSeconds)
pyautogui.press('*', _pause=pauseSeconds)
pyautogui.press('3', _pause=pauseSeconds)
pyautogui.press('enter', _pause=pauseSeconds)

# Division
pyautogui.press('escape', _pause=pauseSeconds)
pyautogui.press('7', _pause=pauseSeconds)
pyautogui.press('/', _pause=pauseSeconds)
pyautogui.press('3', _pause=pauseSeconds)
pyautogui.press('enter', _pause=pauseSeconds)

# Close Calculator
pyautogui.press('escape', _pause=pauseSeconds)
pyautogui.hotkey('alt', 'f4')