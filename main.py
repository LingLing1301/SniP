from PIL import ImageGrab
import keyboard,datetime,os,pyautogui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QApplication

# 监听按键

def screenshot():os.system("glogal.py")
keyboard.add_hotkey('f1', screenshot)

def area():os.system("area.py")
keyboard.add_hotkey('f2', area)

def pas():os.system("pas.py")
keyboard.add_hotkey('f3', pas)

def colora():os.system("Colora.exe")
keyboard.add_hotkey('f4', colora)

keyboard.wait()






























