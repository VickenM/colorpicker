from PySide6 import QtCore, QtGui, QtWidgets


class ColorWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.set_color(QtGui.QColor('#000000'))

    def set_color(self, color:QtGui.QColor):
        image = QtGui.QImage(1, 1, QtGui.QImage.Format_RGB888)
        image.fill(color)
        self.setPixmap(QtGui.QPixmap.fromImage(image).scaled(self.width(), self.height()))

    def get_color(self):
        return self.pixmap().toImage().pixelColor(QtCore.QPoint(0,0))

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.setPixmap(self.pixmap().scaled(self.width(), self.height()))
