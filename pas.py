from PIL import ImageGrab
import keyboard,datetime,os
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 加载并缩放图片
        self.image = QImage(os.path.dirname(os.path.abspath(__file__))+"\\screenshot.png")
        self.scale_factor = 1.0  # 缩放因子
        self.scaled_image = self.image.scaled(
            int(self.image.width() * self.scale_factor),
            int(self.image.height() * self.scale_factor),
            Qt.KeepAspectRatio)

        # 设置窗口大小
        self.setFixedSize(self.scaled_image.width(), self.scaled_image.height())
        
        # 监听快捷键
        keyboard.add_hotkey('f3', self.toggle_visibility)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            # 将窗口移动到屏幕中心
            screen_rect = QApplication.desktop().screenGeometry()
            self.move(screen_rect.center() - self.rect().center())

    def paintEvent(self, event):
        QPainter(self).drawPixmap(QPoint(0, 0), QPixmap.fromImage(self.scaled_image))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def wheelEvent(self, event):
        # 更新缩放因子
        self.scale_factor += 0.1 if event.angleDelta().y() > 0 else -0.1
        self.scale_factor = max(self.scale_factor, 0.1)

        # 缩放图片并更新窗口大小
        self.scaled_image = self.image.scaled(
            int(self.image.width() * self.scale_factor),
            int(self.image.height() * self.scale_factor),
            Qt.KeepAspectRatio
        )
        self.setFixedSize(self.scaled_image.width(), self.scaled_image.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()