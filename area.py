from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import keyboard,datetime,os,pyautogui


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowState(Qt.WindowFullScreen)
        self.setMouseTracking(True)

        # 取消默认的背景色
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.transparent)
        self.setPalette(p)

        # 保存截图的起点和终点
        self.begin = QPoint()
        self.end = QPoint()

    def paintEvent(self, event):
        # 获取当前窗口
        screen = QApplication.primaryScreen()
        if not screen:
            return

        # 获取窗口大小
        pixmap = screen.grabWindow(QApplication.desktop().winId())

        # 创建画布
        painter = QPainter(self)

        # 绘制背景
        painter.drawPixmap(self.rect(), pixmap)

        # 绘制截图矩形
        if not self.begin.isNull() and not self.end.isNull():
            rect = QRect(self.begin, self.end)
            painter.fillRect(rect, QColor(0, 0, 0, 0))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # 截图完成，保存图片
            pixmap = QApplication.primaryScreen().grabWindow(
                QApplication.desktop().winId(),
                self.begin.x(),
                self.begin.y(),
                self.end.x() - self.begin.x(),
                self.end.y() - self.begin.y()
            )
            dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"截图{dt}.png"
            pixmap.save(os.path.dirname(os.path.abspath(__file__))+f"\\{filename}")
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


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()