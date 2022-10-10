from PySide6 import QtCore, QtGui, QtWidgets
def get_color_saturation_and_value_image()->QtGui.QImage:
    image = QtGui.QImage(255, 255, QtGui.QImage.Format_RGB888)
    image.fill(QtGui.QColor(0,0,0))
    
    c = QtGui.QColor()
    for s_x in range(255):
        for v_y in range(0, 255):
            c.setHsv(0, s_x, 255 - v_y)
            image.setPixelColor(s_x, v_y, c)

    return image

class SaturationValueWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_saturation_and_value_image()
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
        painter.setRenderHint(painter.Antialiasing)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        pen.setWidth(2)
        painter.setPen(pen)

        painter.setBrush(QtCore.Qt.NoBrush)
        if self.click_pos:
            painter.drawEllipse(self.click_pos, 10, 10)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = SaturationValueWidget()
    main.show()
    app.exec()
