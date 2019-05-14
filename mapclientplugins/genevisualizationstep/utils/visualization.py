import sys

import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pandas as pd


class Visualization:

    def __init__(self, data):
        self._data = data
        # self._app = QtGui.QApplication([])
        self._w = None

    def viewTable(self):
        self._w = pg.TableWidget()
        self._w.show()
        self._w.resize(500, 500)
        self._w.setWindowTitle("Table for the %s RNASeq data" % self._data['data'])

        # re-structure the data frame into a numpy array
        darray = np.hstack((np.asarray(self._data['id'], dtype=object).reshape(len(self._data['id']), 1),
                            np.asarray(self._data['gene'], dtype=float)))
        a = pd.concat((self._data['id'], self._data['gene']), axis=1)
        self._w.setData(np.asarray(darray))
        b = ['Sample Name'] + self._data['gene'].columns.values.tolist()
        self._w.setHorizontalHeaderLabels(([a for a in b]))
        # if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        #     QtGui.QApplication.instance().exec_()


