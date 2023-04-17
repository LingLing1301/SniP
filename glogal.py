from PIL import ImageGrab
import keyboard,datetime,os,pyautogui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QApplication

# 截取全屏
screenshot = ImageGrab.grab()

# 生成文件名
now = datetime.datetime.now()
desktop = os.path.dirname(os.path.abspath(__file__))
file_name = "screenshot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
file_path = os.path.join(desktop, file_name)

# 保存截图
screenshot.save(file_path)