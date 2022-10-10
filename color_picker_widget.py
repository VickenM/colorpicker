from PySide6 import QtCore, QtGui, QtWidgets

from hue_widget import HueWidget
from saturation_value_widget import SaturationValueWidget

class ColorPickerWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget|None = None):
        super().__init__(parent=parent)

        self.hue_widget = HueWidget()
        self.hue_widget.setMinimumSize(QtCore.QSize(100, 10))
        self.hue_widget.setMaximumHeight(20)

        self.saturation_value_widget = SaturationValueWidget()
        self.saturation_value_widget.setMinimumSize(QtCore.QSize(100, 100))

        self._init_layout()
       
    def _init_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.saturation_value_widget)
        layout.addWidget(self.hue_widget)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    widget = ColorPickerWidget()
    widget.show()
    app.exec()
