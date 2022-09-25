from PySide6 import QtCore, QtGui, QtWidgets

class Main(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setPixmap(self.get_pixmap().scaled(self.width(), 50))

    def get_pixmap(self):
        width = 360
        height = 50
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB888)
        image.fill(QtGui.QColor(0,0,0))
        
        c = QtGui.QColor('#ff0000')
        for x in range(360):
            for y in range(height):
                image.setPixelColor(x, y, c)
            h,s,v,l = c.getHsv()
            c.setHsv(h+1, s, v, l)

        return QtGui.QPixmap.fromImage(image)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = Main()
    main.show()
    app.exec()
