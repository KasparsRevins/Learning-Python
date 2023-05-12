from pyautogui import *
import pyautogui
import win32api, win32con


def click():
    win32api.keybd_event(win32con.VK_SPACE, 0, 0, 0)

while True:
    if pyautogui.pixelMatchesColor(353, 415, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(571, 443, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(610, 521, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(614, 612, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(650, 610, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(581, 400, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(375, 691, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(320, 614, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(322, 528, (120, 120, 122),tolerance=15):
        click()
    if pyautogui.pixelMatchesColor(373, 428, (120, 120, 122),tolerance=15):
        click()
