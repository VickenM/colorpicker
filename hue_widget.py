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
    def __init__(self):
        super().__init__()
        self.image: QtGui.QImage = get_color_hue_image()
        self._pixmap = QtGui.QPixmap.fromImage(self.image)
        #self.setPixmap(self._pixmap)
        self.click_pos = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setPixmap(self._pixmap.scaled(self.width(), self.height()))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.click_pos = event.position().toPoint()
        image = self.pixmap().toImage()
        color = image.pixelColor(self.click_pos)
        print(event.position().toPoint(), color)
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
            painter.drawLine(self.click_pos.x(), 0, self.click_pos.x(), self.height())
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = HueWidget()
    main.show()
    app.exec()
