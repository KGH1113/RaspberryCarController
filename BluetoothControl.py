import pyautogui

class ScreenControling:
    def __init__(self):
        self.go = (1400, 167)
        self.back = (1400, 230)
        self.left = (1400, 300)
        self.right = (1400, 360)
        self.stop = (1400, 421)
        self.alert = (840, 600)

    def click_go(self):
        pyautogui.moveTo(self.go)
        pyautogui.click()
        pyautogui.moveTo(self.alert)
        pyautogui.click()

    def click_back(self):
        pyautogui.moveTo(self.back)
        pyautogui.click()
        pyautogui.moveTo(self.alert)
        pyautogui.click()

    def click_left(self):
        pyautogui.moveTo(self.left)
        pyautogui.click()
        pyautogui.moveTo(self.alert)
        pyautogui.click()

    def click_right(self):
        pyautogui.moveTo(self.right)
        pyautogui.click()
        pyautogui.moveTo(self.alert)
        pyautogui.click()

    def click_stop(self):
        pyautogui.moveTo(self.stop)
        pyautogui.click()
        pyautogui.moveTo(self.alert)
        pyautogui.click()

if __name__ == '__main__':
    while True:
        print(pyautogui.position())