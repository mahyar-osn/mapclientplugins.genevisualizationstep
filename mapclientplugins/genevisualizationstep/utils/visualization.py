import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class Visualization:

    def __init__(self, data):
        self._data = data
        self._app = QtGui.QApplication([])
        self._w = pg.TableWidget()
        self._w.show()
        self._w.resize(500, 500)
        self._w.setWindowTitle("")
