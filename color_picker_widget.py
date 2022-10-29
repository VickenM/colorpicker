from PySide6 import QtCore, QtGui, QtWidgets

from hue_widget import HueWidget
from saturation_value_widget import SaturationValueWidget
from color_widget import ColorWidget

class ColorInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self._color = QtGui.QColor()
        
        self.rgb_label = QtWidgets.QLabel()
        self.hsv_label = QtWidgets.QLabel()
        self.hex_label = QtWidgets.QLabel()

        self._init_layout()

    def _init_layout(self):
        rgb_layout = QtWidgets.QHBoxLayout()
        rgb_layout.addWidget(QtWidgets.QLabel('RGB'))
        rgb_layout.addWidget(self.rgb_label)

        hsv_layout = QtWidgets.QHBoxLayout()
        hsv_layout.addWidget(QtWidgets.QLabel('HSV'))
        hsv_layout.addWidget(self.hsv_label)

        hex_layout = QtWidgets.QHBoxLayout()
        hex_layout.addWidget(QtWidgets.QLabel('HEX'))
        hex_layout.addWidget(self.hex_label)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(rgb_layout)
        layout.addLayout(hsv_layout)
        layout.addLayout(hex_layout)

        self.setLayout(layout)

    def set_color(self, color):
        self._color = color
        self.rgb_label.setText(','.join([str(c) for c in self._color.getRgb()]))
        self.hsv_label.setText(','.join([str(c) for c in self._color.getHsv()]))
        self.hex_label.setText(self._color.name())

class ColorPickerWidget(QtWidgets.QWidget):
    current_color = QtCore.Signal(QtGui.QColor)
    def __init__(self, parent = None):
        super().__init__(parent=parent)

        self.hue_widget = HueWidget()
        self.hue_widget.setMinimumSize(QtCore.QSize(100, 20))
        self.hue_widget.setMaximumHeight(20)

        self.saturation_value_widget = SaturationValueWidget()
        self.saturation_value_widget.setMinimumSize(QtCore.QSize(100, 100))

        self.color_widget = ColorWidget()
        self.color_widget.setFixedSize(QtCore.QSize(100, 100))

        self.color_info_widget = ColorInfoWidget()

        self._init_connections()
        self._init_layout()
   
    def _init_layout(self):
        picker_layout = QtWidgets.QVBoxLayout()
        picker_layout.addWidget(self.saturation_value_widget)
        picker_layout.addWidget(self.hue_widget)

        preview_layout = QtWidgets.QHBoxLayout()
        preview_layout.addWidget(self.color_widget)
        preview_layout.addLayout(picker_layout)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(preview_layout, stretch=1)
        layout.addWidget(self.color_info_widget)

        self.setLayout(layout)

    def _init_connections(self):
        self.hue_widget.color_changed.connect(self.on_hue_color_changed)
        self.saturation_value_widget.color_changed.connect(self.on_saturation_value_color_changed)

    def on_hue_color_changed(self, color:QtGui.QColor):
        hue, _, _, _ = color.getHsv()
        self.saturation_value_widget.set_hue(hue)
        self.current_color.emit(color)

    def on_saturation_value_color_changed(self, color: QtGui.QColor):
        self.set_color_widget(color)
        self.current_color.emit(color)

    def set_color_widget(self, color: QtGui.QColor):
        self.color_widget.set_color(color)
        self.color_info_widget.set_color(color)

    def set_color(self, color:QtGui.QColor):
        self.hue_widget.set_color(color)
        self.saturation_value_widget.set_color(color)


if __name__ == '__main__':
    def on_color_changed(color):
        print(color)

    app = QtWidgets.QApplication()
    widget = ColorPickerWidget()
    widget.current_color.connect(on_color_changed)
    widget.show()
    widget.set_color(QtGui.QColor(25, 55, 30))
    app.exec()
