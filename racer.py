from pyautogui import press, typewrite, hotkey
import time
import pygetwindow as gw
 

window = gw.getWindowsWithTitle('Google Docs')[0]
window.activate()

time.sleep(2)
press('a  ')
typewrite(' The sun dipped below the horizon, casting a warm golden hue over the calm ocean. Waves gently lapped at the shore, their rhythmic sound blending with the soft breeze that carried the scent of saltwater. In the distance, seagulls soared effortlessly, their calls echoing across the vast expanse of the sky. The day had been long, but as the stars began to emerge, there was a sense of peace, as though the world itself was settling into a quiet, restful slumber.'t interval=1)
time.sleep(1)
hotkey('ctrl', 'x')