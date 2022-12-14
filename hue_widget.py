from PySide6 import QtCore, QtGui, QtWidgets


def get_color_hue_image()->QtGui.QImage:
    image = QtGui.QImage(360, 1, QtGui.QImage.Format_RGB888)
    image.fill(QtGui.QColor('#000000'))
    
    c = QtGui.QColor('#ff0000')
    for x in range(360):
        image.setPixelColor(x, 0, c)
        hue, saturation, value, alpha = c.getHsv()
        c.setHsv(hue + 1, saturation, value, alpha)

    return image

class HueWidget(QtWidgets.QLabel):
    color_changed = QtCore.Signal(QtGui.QColor)

    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_hue_image()
        self._pixmap = QtGui.QPixmap.fromImage(self.image)
        self._position = QtCore.QPointF(0.0, 0.0)
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))

    def set_position(self, position):
        self._position = position
        self.color_changed.emit(self.get_color())
        self.repaint()

    def get_point(self):
        x = int(self.width() * self._position.x())
        x = max(0, min(x, self.width()-1))

        y = int(self.height() * self._position.y())
        y = max(0, min(y, self.height()-1))
        return QtCore.QPoint(x,y)

    def get_color(self):
        color = self.pixmap().toImage().pixelColor(self.get_point())
        return color

    def set_color(self, color:QtGui.QColor):
        hue, _, _, _ = color.getHslF()
        self._position.setX(hue)
        self.color_changed.emit(self.get_color())

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        click_pos = event.position().toPoint()
        position = QtCore.QPointF(click_pos.x()/ self.width(), click_pos.y()/self.height())
        self.set_position(position)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

        if event.buttons() & QtCore.Qt.LeftButton:
            click_pos = event.position().toPoint()
            position = QtCore.QPointF(click_pos.x()/ self.width(), click_pos.y()/self.height())
            self.set_position(position)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QtGui.QPainter(self)

        pen = QtGui.QPen(QtGui.QColor('#ffffff'))
        pen.setWidth(1)
        painter.setPen(pen)

        point = self.get_point()
        painter.drawLine(point.x(), 0, point.x(), self.height())
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = HueWidget()
    main.show()
    app.exec()
