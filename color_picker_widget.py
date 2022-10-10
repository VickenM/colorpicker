from PySide6 import QtCore, QtGui, QtWidgets

from hue_widget import HueWidget
from saturation_value_widget import SaturationValueWidget

class ColorPickerWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget|None = None):
        super().__init__(parent=parent)

        self.hue_widget = HueWidget()
        self.hue_widget.setMinimumSize(QtCore.QSize(100, 20))
        self.hue_widget.setMaximumHeight(20)

        self.saturation_value_widget = SaturationValueWidget()
        self.saturation_value_widget.setMinimumSize(QtCore.QSize(100, 100))

        self._init_connections()
        self._init_layout()
   
#        color = self.hue_widget.get_color()
        self.saturation_value_widget.set_position(QtCore.QPointF(0.25, 0.1))

        #self.saturation_value_widget.setFixedSize(700, 200)

    def _init_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.saturation_value_widget)
        layout.addWidget(self.hue_widget)

        self.setLayout(layout)

    def _init_connections(self):
        self.hue_widget.color_changed.connect(self.on_hue_color_changed)

    def on_hue_color_changed(self, color:QtGui.QColor):
        print(color)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    widget = ColorPickerWidget()
    widget.show()
    app.exec()
