# importing the modules
from PIL import Image,ImageGrab
import pyautogui
import time


def Click(key):
    pyautogui.keyDown(key)
    return





def isCollide(data):
    for i in range(530,620):
        for j in range(620,450):
            if data[i, j] < 100:
                Click('up')
                return
    for i in range(452,729):
        for j in range(646,343):
            if data[i,j] < 171:
                Click('down')
                return
    return
if __name__=='__main__':
    time.sleep(5)
    Click('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        # Draw the rectangle for cactus
        for i in range(520,610):
            for j in range(130, 160):
                data[i, j] = 0

        # # Draw the rectangle for birds
        for i in range(510, 560):
            for j in range(100, 125):
                data[i, j] = 171

        image.show()