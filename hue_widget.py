from PySide6 import QtCore, QtGui, QtWidgets
def get_color_hue_image()->QtGui.QImage:
    width = 360
    image = QtGui.QImage(width, 1, QtGui.QImage.Format_RGB888)
    image.fill(QtGui.QColor(0,0,0))
    
    c = QtGui.QColor('#ff0000')
    for x in range(width):
        image.setPixelColor(x, 0, c)
        h,s,v,l = c.getHsv()
        c.setHsv(h+1, s, v, l)

    return image
    return QtGui.QPixmap.fromImage(image)

class HueWidget(QtWidgets.QLabel):
    color_changed = QtCore.Signal(QtGui.QColor)

    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_hue_image()
        self._pixmap = QtGui.QPixmap.fromImage(self.image)
        self._click_pos = QtCore.QPoint(0, 0)

    def get_color(self):
        image = self.pixmap().toImage()
        color = image.pixelColor(self._click_pos)
        return color

    def set_color(self, color:QtGui.QColor):
        hue, saturation, lightness, alpha = color.getHsl()
        self._click_pos.setX(int((hue * 255) / 360))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self._click_pos = event.position().toPoint()
        self.color_changed.emit(self.get_color())
        self.repaint()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if event.buttons() & QtCore.Qt.LeftButton:
            self._click_pos = event.position().toPoint()
            self.color_changed.emit(self.get_color())
            self.repaint()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QtGui.QPainter(self)
#        painter.setRenderHint(painter.Antialiasing)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        pen.setWidth(1)
        painter.setPen(pen)

#        painter.setBrush(QtCore.Qt.black)
        if self._click_pos:
            painter.drawLine(self._click_pos.x(), 0, self._click_pos.x(), self.height())
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = HueWidget()
    main.show()
    app.exec()
