# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geneview.ui'
#
# Created: Tue May 14 16:49:26 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_GeneVisualizationWidget(object):
    def setupUi(self, GeneVisualizationWidget):
        GeneVisualizationWidget.setObjectName("GeneVisualizationWidget")
        GeneVisualizationWidget.resize(833, 632)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeneVisualizationWidget.sizePolicy().hasHeightForWidth())
        GeneVisualizationWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(GeneVisualizationWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(GeneVisualizationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(346, 135))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 344, 608))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtGui.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setStyleSheet("QToolBox::tab {\n"
                                   "         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                   "                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                   "         border-radius: 5px;\n"
                                   "         color: black;\n"
                                   "     }\n"
                                   "\n"
                                   "     QToolBox::tab:selected { /* italicize selected tabs */\n"
                                   "         font: bold;\n"
                                   "         color: black;\n"
                                   "     }\n"
                                   "QToolBox {\n"
                                   "    padding : 0\n"
                                   "}")
        self.toolBox.setObjectName("toolBox")
        self.genePage = QtGui.QWidget()
        self.genePage.setGeometry(QtCore.QRect(0, 0, 340, 548))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genePage.sizePolicy().hasHeightForWidth())
        self.genePage.setSizePolicy(sizePolicy)
        self.genePage.setObjectName("genePage")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.genePage)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ViewGroupBox = QtGui.QGroupBox(self.genePage)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.ViewGroupBox.setFont(font)
        self.ViewGroupBox.setCheckable(False)
        self.ViewGroupBox.setObjectName("ViewGroupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.ViewGroupBox)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.viewerWidgets = QtGui.QWidget(self.ViewGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewerWidgets.sizePolicy().hasHeightForWidth())
        self.viewerWidgets.setSizePolicy(sizePolicy)
        self.viewerWidgets.setObjectName("viewerWidgets")
        self.gridLayout = QtGui.QGridLayout(self.viewerWidgets)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.viewXMLButton = QtGui.QPushButton(self.viewerWidgets)
        self.viewXMLButton.setEnabled(True)
        self.viewXMLButton.setObjectName("viewXMLButton")
        self.gridLayout.addWidget(self.viewXMLButton, 0, 1, 1, 1)
        self.viewScaffoldButton = QtGui.QPushButton(self.viewerWidgets)
        self.viewScaffoldButton.setEnabled(True)
        self.viewScaffoldButton.setObjectName("viewScaffoldButton")
        self.gridLayout.addWidget(self.viewScaffoldButton, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.viewerWidgets)
        self.line_3 = QtGui.QFrame(self.ViewGroupBox)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.line_2 = QtGui.QFrame(self.ViewGroupBox)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.line = QtGui.QFrame(self.ViewGroupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.cellGeneWidgets = QtGui.QWidget(self.ViewGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cellGeneWidgets.sizePolicy().hasHeightForWidth())
        self.cellGeneWidgets.setSizePolicy(sizePolicy)
        self.cellGeneWidgets.setObjectName("cellGeneWidgets")
        self.formLayout = QtGui.QFormLayout(self.cellGeneWidgets)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.cellSelectLabel = QtGui.QLabel(self.cellGeneWidgets)
        self.cellSelectLabel.setObjectName("cellSelectLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cellSelectLabel)
        self.cellSelectcomboBox = QtGui.QComboBox(self.cellGeneWidgets)
        self.cellSelectcomboBox.setObjectName("cellSelectcomboBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cellSelectcomboBox)
        self.geneSelectLabel = QtGui.QLabel(self.cellGeneWidgets)
        self.geneSelectLabel.setObjectName("geneSelectLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.geneSelectLabel)
        self.comboBox = QtGui.QComboBox(self.cellGeneWidgets)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout_7.addWidget(self.cellGeneWidgets)
        self.verticalLayout_5.addWidget(self.ViewGroupBox)
        self.plotGroupBox = QtGui.QGroupBox(self.genePage)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.plotGroupBox.setFont(font)
        self.plotGroupBox.setCheckable(False)
        self.plotGroupBox.setObjectName("plotGroupBox")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.plotGroupBox)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.viewerWidgets_2 = QtGui.QWidget(self.plotGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewerWidgets_2.sizePolicy().hasHeightForWidth())
        self.viewerWidgets_2.setSizePolicy(sizePolicy)
        self.viewerWidgets_2.setObjectName("viewerWidgets_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.viewerWidgets_2)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_8.addWidget(self.viewerWidgets_2)
        self.dataTablepushButton = QtGui.QPushButton(self.plotGroupBox)
        self.dataTablepushButton.setObjectName("dataTablepushButton")
        self.verticalLayout_8.addWidget(self.dataTablepushButton)
        self.barPlotpushButton = QtGui.QPushButton(self.plotGroupBox)
        self.barPlotpushButton.setObjectName("barPlotpushButton")
        self.verticalLayout_8.addWidget(self.barPlotpushButton)
        self.heatMappushButton = QtGui.QPushButton(self.plotGroupBox)
        self.heatMappushButton.setObjectName("heatMappushButton")
        self.verticalLayout_8.addWidget(self.heatMappushButton)
        self.checkBox = QtGui.QCheckBox(self.plotGroupBox)
        self.checkBox.setMinimumSize(QtCore.QSize(20, 0))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_8.addWidget(self.checkBox)
        self.line_4 = QtGui.QFrame(self.plotGroupBox)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.line_5 = QtGui.QFrame(self.plotGroupBox)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.line_6 = QtGui.QFrame(self.plotGroupBox)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_8.addWidget(self.line_6)
        self.verticalLayout_5.addWidget(self.plotGroupBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.toolBox.addItem(self.genePage, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewAllButton = QtGui.QPushButton(self.frame)
        self.viewAllButton.setObjectName("viewAllButton")
        self.horizontalLayout_2.addWidget(self.viewAllButton)
        self.doneButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout_2.addWidget(self.doneButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.sceneviewerWidget = BaseSceneviewerWidget(GeneVisualizationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy)
        self.sceneviewerWidget.setObjectName("sceneviewerWidget")
        self.horizontalLayout.addWidget(self.sceneviewerWidget)

        self.retranslateUi(GeneVisualizationWidget)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(2)
        QtCore.QMetaObject.connectSlotsByName(GeneVisualizationWidget)

    def retranslateUi(self, GeneVisualizationWidget):
        GeneVisualizationWidget.setWindowTitle(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("GeneVisualizationWidget", "RNA-Seq Mapping", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.ViewGroupBox.setTitle(
            QtGui.QApplication.translate("GeneVisualizationWidget", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.viewXMLButton.setToolTip(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Show MBF segmented data", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.viewXMLButton.setText(QtGui.QApplication.translate("GeneVisualizationWidget", "XML/EX data", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.viewScaffoldButton.setToolTip(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Show scaffold", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.viewScaffoldButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Scaffold", None, QtGui.QApplication.UnicodeUTF8))
        self.cellSelectLabel.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Cells:", None, QtGui.QApplication.UnicodeUTF8))
        self.geneSelectLabel.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Genes:", None, QtGui.QApplication.UnicodeUTF8))
        self.plotGroupBox.setTitle(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTablepushButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.barPlotpushButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.heatMappushButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Heatmap", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.genePage),
                                 QtGui.QApplication.translate("GeneVisualizationWidget", "Control Panel", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.viewAllButton.setToolTip(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Adjust the view to see the whole model", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.viewAllButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setToolTip(QtGui.QApplication.translate("GeneVisualizationWidget", "Finish this step", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(
            QtGui.QApplication.translate("GeneVisualizationWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))


from opencmiss.zincwidgets.basesceneviewerwidget import BaseSceneviewerWidget
