import keyboard,os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.image = QImage(os.path.abspath("screenshot.png"))
        self.scale_factor = 1.0
        self.scaled_image = self.image.scaled(
        int(self.image.width() * self.scale_factor),
        int(self.image.height() * self.scale_factor),
        Qt.KeepAspectRatio)
        self.setFixedSize(self.scaled_image.width(), self.scaled_image.height())
        keyboard.add_hotkey('f3', self.toggle_visibility)

    def toggle_visibility(self):
        self.setVisible(not self.isVisible())
        if self.isVisible():
            self.move(QApplication.desktop().screenGeometry().center() - self.rect().center())

    def paintEvent(self, event):
        QPainter(self).drawPixmap(QPoint(), QPixmap.fromImage(self.scaled_image))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def wheelEvent(self, event):
        self.scale_factor += 0.1 if event.angleDelta().y() > 0 else -0.1
        self.scale_factor = max(self.scale_factor, 0.1)
        self.scaled_image = self.image.scaled(
            int(self.image.width() * self.scale_factor),
            int(self.image.height() * self.scale_factor),
            Qt.KeepAspectRatio)
        self.setFixedSize(self.scaled_image.width(), self.scaled_image.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

app = QApplication([])
widget = MyWidget()
widget.show()
app.exec_()