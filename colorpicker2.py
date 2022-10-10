from PySide6 import QtCore, QtGui, QtWidgets
def get_color_hue_image()->QtGui.QImage:
    image = QtGui.QImage(200, 200, QtGui.QImage.Format_RGB888)
    image.fill(QtGui.QColor(0,0,0))
    
    c = QtGui.QColor()
    for s_x in range(200):
        for l_y in range(0, 200):
            c.setHsvF(240/360, s_x/200, 1-l_y/200)
            image.setPixelColor(s_x, l_y, c)

    return image

class Main(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_hue_image()
        self._pixmap: QtGui.QPixmap = QtGui.QPixmap.fromImage(self.image)
        self.setPixmap(self._pixmap)
        self.click_pos = None


    def resizeEvent(self, event):
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))
        return super().resizeEvent(event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        image = self._pixmap.toImage()
        c = image.pixelColor(event.position().toPoint())
        print(event.position().toPoint(), c)
        self.click_pos = event.position().toPoint()
        self.repaint()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if event.buttons() & QtCore.Qt.LeftButton:
            self.click_pos = event.position().toPoint()
            self.repaint()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QtGui.QPainter(self)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        pen.setWidth(1)
        painter.setPen(pen)

        painter.setBrush(QtCore.Qt.NoBrush)
        if self.click_pos:
            painter.drawLine(self.click_pos.x(), 0, self.click_pos.x(), self.height())
            painter.drawEllipse(self.click_pos, 10, 10)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = Main()
    main.show()
    app.exec()
