from PySide6 import QtCore, QtGui, QtWidgets

class ColorWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._color = QtGui.QColor()
        self.set_color(QtGui.QColor(0, 0, 0))

    def set_color(self, color:QtGui.QColor):
        self._color = color
        image = QtGui.QImage(10, 10, QtGui.QImage.Format_RGB888)
        image.fill(self._color)

        self.setPixmap(QtGui.QPixmap.fromImage(image).scaled(self.width(), self.height()))

    def get_color(self):
        self._color

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setPixmap(self.pixmap().scaled(self.width(), self.height()))
