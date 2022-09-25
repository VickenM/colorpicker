from PySide6 import QtCore, QtGui, QtWidgets

class Main(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setPixmap(self.get_pixmap())

    def get_pixmap(self):
        width = 500
        height = 50
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB888)
        image.fill(QtGui.QColor(0,0,0))
        
        from math import floor
        step = 255/ (width / 6)
        step = floor(step)
        final = False

        r,g,b = 255,0,0
        for x in range(width):
            if not final:
                if b == 0:
                    g = min(g+step, 255)
                if b == 255:
                    g = max(g-step, 0)
                if g == 255:
                    r = max(r-step, 0)
                if r == 0:
                    b = min (b+step, 255)
                if g == 255 and b == 255:
                    r = min(r+step, 255)
                if r == step and g == 0 and b == 255:
                    final = True
            else:
                r = min (r+step, 255)
                if r == 255:
                    b = max (b-step, 0)

            for y in range(height):
                image.setPixelColor(x, y, QtGui.QColor(r,g,b))
        

        return QtGui.QPixmap.fromImage(image)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = Main()
    main.show()
    app.exec()
