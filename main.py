from PIL import ImageGrab
import keyboard,datetime,os

def scs():
 ImageGrab.grab().save(os.path.join(os.path.dirname(os.path.abspath(__file__)),datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".png"))
keyboard.add_hotkey('f1',scs)

def area():os.system("area.py")
keyboard.add_hotkey('f2', area)

def pas():os.system("pas.py")
keyboard.add_hotkey('f3', pas)

def colora():os.system("Colora.exe")
keyboard.add_hotkey('f4', colora)

keyboard.wait()

