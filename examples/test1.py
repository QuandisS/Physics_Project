import numpy as np
import pyqtgraph as pg
from PyQt5 import  QtCore

plot = pg.plot()

s = pg.PlotCurveItem()

plot.addItem(s)


x = np.array([1, 2, 3])
y = np.array([1, 2, 3])

app_x = np.array([4])
app_y = np.array([4])

x = np.hstack((x, app_x))
y = np.hstack((y, app_y))
print(x)
print(y)

s.setData(x=x, y=y)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()