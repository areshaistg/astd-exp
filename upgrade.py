import pyautogui
import time
import keyboard
import random
import win32api, win32con
import autoit

# Inventory (X: 55, Y: 464)
# Search Bar (X: 868, Y: 272, 198, 244, 255)

BACKPACK_LOCATION = (55, 464)
SEARCH_BAR_LOCATION = (868, 272)
SEARCH_BAR_COLOR = (198, 244, 255)
INVENTORY_REGION = (709, 241, 1204-709, 791-241)
EVOLVE_LOCATION = (905, 376)
UPGRADE_LOCATION = (956, 640)
CAN_EVOLVE_LOCATION = (545, 856)

def click(x, y):
    # win32api.SetCursorPos((x, y))
    pyautogui.moveTo(x, y, 1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)


def evolve_exp(fileName):
    searchBarPixel = pyautogui.pixel(SEARCH_BAR_LOCATION[0], SEARCH_BAR_LOCATION[1])
    if searchBarPixel != SEARCH_BAR_COLOR:
        # click(BACKPACK_LOCATION[0], BACKPACK_LOCATION[1])
        autoit.mouse_click('left', BACKPACK_LOCATION[0], BACKPACK_LOCATION[1])
        time.sleep(0.25)

    ret = pyautogui.locateOnScreen(fileName, region=INVENTORY_REGION, grayscale=True, confidence=1)
    if ret != None:
        pos = (ret.left + ret.width / 2, ret.top + ret.height / 2)
        autoit.mouse_click('left', int(pos[0]), int(pos[1]))
        time.sleep(0.1)
        autoit.mouse_click('left', EVOLVE_LOCATION[0], EVOLVE_LOCATION[1])
        if pyautogui.pixel(CAN_EVOLVE_LOCATION[0], CAN_EVOLVE_LOCATION[1])[0] == 255:
            autoit.mouse_click('left', UPGRADE_LOCATION[0], UPGRADE_LOCATION[1])
            time.sleep(0.25)
            autoit.mouse_click('left', UPGRADE_LOCATION[0], UPGRADE_LOCATION[1])
            return True

    return False

foundExp1 = True
foundExp2 = True
foundExp3 = True

while keyboard.is_pressed('q') == False:
    if foundExp1:
        foundExp1 = evolve_exp('images/exp1.png')

    if foundExp2:
        foundExp2 = evolve_exp('images/exp2.png')

    if foundExp3:
        foundExp3 = evolve_exp('images/exp3.png')

    if not foundExp1 and not foundExp2 and not foundExp3:
        break
