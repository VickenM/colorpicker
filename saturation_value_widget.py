from PySide6 import QtCore, QtGui, QtWidgets
def get_color_saturation_and_value_image(hue: int)->QtGui.QImage:
    image = QtGui.QImage(255, 255, QtGui.QImage.Format_RGB888)
    image.fill(QtGui.QColor(0,0,0))
    
    c = QtGui.QColor()
    for s_x in range(255):
        for v_y in range(0, 255):
            c.setHsv(hue, s_x, 255 - v_y)
            image.setPixelColor(s_x, v_y, c)

    return image

class SaturationValueWidget(QtWidgets.QLabel):
    color_changed = QtCore.Signal(QtGui.QColor)

    def __init__(self):
        super().__init__()
        self._pixmap: QtGui.QPixmap = QtGui.QPixmap()
        self._pos = QtCore.QPointF(0.0, 0.0)
        
        self.setHue(hue=0)

    def setHue(self, hue):
        image: QtGui.QImage = get_color_saturation_and_value_image(hue)
        self._pixmap: QtGui.QPixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))
        self.color_changed.emit(self.get_color())

    @property
    def _point(self):
        x = int(self.width() * self._pos.x())
        x = max(0, min(x, self.width()-1))

        y = int(self.height() * self._pos.y())
        y = max(0, min(y, self.height()-1))
        return QtCore.QPoint(x, y)

    def get_color(self):
        color = self.pixmap().toImage().pixelColor(self._point)
        return color

    def set_position(self, position: QtCore.QPointF):
        self._pos = position

    def get_position(self):
        return self._pos

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

#        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawEllipse(self._point, 10, 10)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = SaturationValueWidget()
    main.show()
    app.exec()
