import sys

# from PySide import QtGui as PySideQtGui

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pandas as pd


class VisualizationHandler:

    def __init__(self, data):
        self._data = data
        # self._app = QtGui.QApplication([])
        self._w = None

    def view_table(self):
        self._w = pg.TableWidget()
        self._w.show()
        self._w.resize(1000, 500)
        self._w.setWindowTitle("Table for the %s RNASeq data" % self._data['data'])

        # re-structure the data frame into a numpy array
        darray = np.hstack((np.asarray(self._data['id'], dtype=object).reshape(len(self._data['id']), 1),
                            np.asarray(self._data['gene'], dtype=float)))
        self._w.setData(np.asarray(darray))

        # Cell ID column with different color
        for item in range(len(darray)):
            self._w.item(item, 0).setBackground(QtGui.QColor(100, 100, 150))

        # Setup header with gene IDs
        b = ['Sample Name'] + self._data['gene'].columns.values.tolist()
        header_labels = [a for a in b]
        self._w.setHorizontalHeaderLabels(header_labels)
        self._w.resizeColumnsToContents()

        print('done')

    def view_bar_plot(self):
        pass

    def view_heatmap(self, cluster=False):

        if cluster:
            self._make_cluster()
        pass

    def _make_cluster(self):
        pass
