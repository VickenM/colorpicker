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

class HueWidget(QtWidgets.QLabel):
    color_changed = QtCore.Signal(QtGui.QColor)

    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_hue_image()
        self._pixmap = QtGui.QPixmap.fromImage(self.image)
        self._pos = QtCore.QPointF(0.0, 0.0)

    @property
    def _point(self):
        x = int(self.width() * self._pos.x())
        x = max(0, min(x, self.width()-1))

        y = int(self.height() * self._pos.y())
        y = max(0, min(y, self.height()-1))
        return QtCore.QPoint(x,y)

    def get_color(self):
        color = self.pixmap().toImage().pixelColor(self._point)
        return color

    def set_color(self, color:QtGui.QColor):
        hue, _, _, _ = color.getHslF()
        self._pos.setX(hue)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        click_pos = event.position().toPoint()
        self._pos = QtCore.QPointF(click_pos.x()/ self.width(), click_pos.y()/self.height())
        self.color_changed.emit(self.get_color())
        self.repaint()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if event.buttons() & QtCore.Qt.LeftButton:
            click_pos = event.position().toPoint()
            self._pos = QtCore.QPointF(click_pos.x()/ self.width(), click_pos.y()/self.height())
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
        point = self._point
        painter.drawLine(point.x(), 0, point.x(), self.height())
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = HueWidget()
    main.show()
    app.exec()
