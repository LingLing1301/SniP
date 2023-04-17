from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime, os

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowState(Qt.WindowFullScreen)
        self.setMouseTracking(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.transparent)
        self.setPalette(p)
        self.begin = QPoint()
        self.end = QPoint()

    def paintEvent(self, event):
        pixmap = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), pixmap)
        if not self.begin.isNull() and not self.end.isNull():
            rect = QRect(self.begin, self.end)
            painter.fillRect(rect, QColor(0, 0, 0, 0))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pixmap = QApplication.primaryScreen().grabWindow(
                QApplication.desktop().winId(),
                self.begin.x(),self.begin.y(),
                self.end.x() - self.begin.x(),
                self.end.y() - self.begin.y())
            pixmap.save(os.path.dirname(os.path.abspath(__file__))+"\\"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".png")
            QApplication.quit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.end = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.end = event.pos()
            self.update()

app = QApplication([])
widget = MyWidget()
widget.show()
app.exec_()