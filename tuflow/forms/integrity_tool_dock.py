# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ellis.Symons\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tuflow\forms\integrity_tool_dock.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IntegrityTool(object):
    def setupUi(self, IntegrityTool):
        IntegrityTool.setObjectName("IntegrityTool")
        IntegrityTool.resize(625, 814)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 588, 991))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gbLines = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.gbLines.setCollapsed(False)
        self.gbLines.setSaveCollapsedState(False)
        self.gbLines.setObjectName("gbLines")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbLines)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputLineLayout = QtWidgets.QVBoxLayout()
        self.InputLineLayout.setObjectName("InputLineLayout")
        self.label = QtWidgets.QLabel(self.gbLines)
        self.label.setObjectName("label")
        self.InputLineLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browseInputLines = QtWidgets.QToolButton(self.gbLines)
        self.browseInputLines.setObjectName("browseInputLines")
        self.horizontalLayout.addWidget(self.browseInputLines)
        self.cboInputLines = QtWidgets.QComboBox(self.gbLines)
        self.cboInputLines.setEditable(True)
        self.cboInputLines.setObjectName("cboInputLines")
        self.horizontalLayout.addWidget(self.cboInputLines)
        self.btnAddLines = QtWidgets.QToolButton(self.gbLines)
        self.btnAddLines.setObjectName("btnAddLines")
        self.horizontalLayout.addWidget(self.btnAddLines)
        self.btnRemoveLines = QtWidgets.QToolButton(self.gbLines)
        self.btnRemoveLines.setObjectName("btnRemoveLines")
        self.horizontalLayout.addWidget(self.btnRemoveLines)
        self.InputLineLayout.addLayout(self.horizontalLayout)
        self.lwLines = QtWidgets.QListWidget(self.gbLines)
        self.lwLines.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lwLines.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwLines.setObjectName("lwLines")
        self.InputLineLayout.addWidget(self.lwLines)
        self.verticalLayout_3.addLayout(self.InputLineLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.gbLines)
        self.gbPoints = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.gbPoints.setCollapsed(True)
        self.gbPoints.setObjectName("gbPoints")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbPoints)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InputPointLayout = QtWidgets.QVBoxLayout()
        self.InputPointLayout.setObjectName("InputPointLayout")
        self.label_2 = QtWidgets.QLabel(self.gbPoints)
        self.label_2.setObjectName("label_2")
        self.InputPointLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.browseInputPoints = QtWidgets.QToolButton(self.gbPoints)
        self.browseInputPoints.setObjectName("browseInputPoints")
        self.horizontalLayout_2.addWidget(self.browseInputPoints)
        self.cboInputPoints = QtWidgets.QComboBox(self.gbPoints)
        self.cboInputPoints.setEditable(True)
        self.cboInputPoints.setObjectName("cboInputPoints")
        self.horizontalLayout_2.addWidget(self.cboInputPoints)
        self.btnAddPoints = QtWidgets.QToolButton(self.gbPoints)
        self.btnAddPoints.setObjectName("btnAddPoints")
        self.horizontalLayout_2.addWidget(self.btnAddPoints)
        self.btnRemovePoints = QtWidgets.QToolButton(self.gbPoints)
        self.btnRemovePoints.setObjectName("btnRemovePoints")
        self.horizontalLayout_2.addWidget(self.btnRemovePoints)
        self.InputPointLayout.addLayout(self.horizontalLayout_2)
        self.lwPoints = QtWidgets.QListWidget(self.gbPoints)
        self.lwPoints.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lwPoints.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwPoints.setObjectName("lwPoints")
        self.InputPointLayout.addWidget(self.lwPoints)
        self.verticalLayout_2.addLayout(self.InputPointLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.gbPoints)
        self.gbTables = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.gbTables.setCollapsed(True)
        self.gbTables.setObjectName("gbTables")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbTables)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.InputTableLayout = QtWidgets.QVBoxLayout()
        self.InputTableLayout.setObjectName("InputTableLayout")
        self.label_3 = QtWidgets.QLabel(self.gbTables)
        self.label_3.setObjectName("label_3")
        self.InputTableLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.browseInputTables = QtWidgets.QToolButton(self.gbTables)
        self.browseInputTables.setObjectName("browseInputTables")
        self.horizontalLayout_3.addWidget(self.browseInputTables)
        self.cboInputTables = QtWidgets.QComboBox(self.gbTables)
        self.cboInputTables.setEditable(True)
        self.cboInputTables.setObjectName("cboInputTables")
        self.horizontalLayout_3.addWidget(self.cboInputTables)
        self.btnAddTables = QtWidgets.QToolButton(self.gbTables)
        self.btnAddTables.setObjectName("btnAddTables")
        self.horizontalLayout_3.addWidget(self.btnAddTables)
        self.btnRemoveTables = QtWidgets.QToolButton(self.gbTables)
        self.btnRemoveTables.setObjectName("btnRemoveTables")
        self.horizontalLayout_3.addWidget(self.btnRemoveTables)
        self.InputTableLayout.addLayout(self.horizontalLayout_3)
        self.lwTables = QtWidgets.QListWidget(self.gbTables)
        self.lwTables.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lwTables.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwTables.setObjectName("lwTables")
        self.InputTableLayout.addWidget(self.lwTables)
        self.verticalLayout_4.addLayout(self.InputTableLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_8.addWidget(self.gbTables)
        self.gbDem = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.gbDem.setCheckable(True)
        self.gbDem.setChecked(False)
        self.gbDem.setCollapsed(True)
        self.gbDem.setObjectName("gbDem")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.gbDem)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_11 = QtWidgets.QLabel(self.gbDem)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_20.addWidget(self.label_11)
        self.cboDem = QtWidgets.QComboBox(self.gbDem)
        self.cboDem.setMinimumSize(QtCore.QSize(150, 0))
        self.cboDem.setObjectName("cboDem")
        self.horizontalLayout_20.addWidget(self.cboDem)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.verticalLayout_8.addWidget(self.gbDem)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.Snapping = QtWidgets.QWidget()
        self.Snapping.setObjectName("Snapping")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Snapping)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rbSnapping = QtWidgets.QRadioButton(self.Snapping)
        self.rbSnapping.setObjectName("rbSnapping")
        self.verticalLayout_5.addWidget(self.rbSnapping)
        self.label_5 = QtWidgets.QLabel(self.Snapping)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.cbExclRadius = QtWidgets.QCheckBox(self.Snapping)
        self.cbExclRadius.setChecked(True)
        self.cbExclRadius.setObjectName("cbExclRadius")
        self.horizontalLayout_8.addWidget(self.cbExclRadius)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem5)
        self.label_19 = QtWidgets.QLabel(self.Snapping)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_22.addWidget(self.label_19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem6)
        self.sbExclRadius = QtWidgets.QDoubleSpinBox(self.Snapping)
        self.sbExclRadius.setDecimals(1)
        self.sbExclRadius.setMaximum(99999.0)
        self.sbExclRadius.setProperty("value", 10.0)
        self.sbExclRadius.setObjectName("sbExclRadius")
        self.horizontalLayout_21.addWidget(self.sbExclRadius)
        self.label_16 = QtWidgets.QLabel(self.Snapping)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_21.addWidget(self.label_16)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.cbAutoSnap = QtWidgets.QCheckBox(self.Snapping)
        self.cbAutoSnap.setObjectName("cbAutoSnap")
        self.horizontalLayout_7.addWidget(self.cbAutoSnap)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.sbAutoSnapSearchRadius = QtWidgets.QDoubleSpinBox(self.Snapping)
        self.sbAutoSnapSearchRadius.setDecimals(3)
        self.sbAutoSnapSearchRadius.setMinimum(0.001)
        self.sbAutoSnapSearchRadius.setMaximum(99999.0)
        self.sbAutoSnapSearchRadius.setProperty("value", 1.5)
        self.sbAutoSnapSearchRadius.setObjectName("sbAutoSnapSearchRadius")
        self.horizontalLayout_6.addWidget(self.sbAutoSnapSearchRadius)
        self.label_4 = QtWidgets.QLabel(self.Snapping)
        self.label_4.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 396, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.tabWidget.addTab(self.Snapping, "")
        self.PipeDirection = QtWidgets.QWidget()
        self.PipeDirection.setObjectName("PipeDirection")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.PipeDirection)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.rbPipeDirection = QtWidgets.QRadioButton(self.PipeDirection)
        self.rbPipeDirection.setObjectName("rbPipeDirection")
        self.verticalLayout_6.addWidget(self.rbPipeDirection)
        self.label_6 = QtWidgets.QLabel(self.PipeDirection)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.cbBasedOnInverts = QtWidgets.QCheckBox(self.PipeDirection)
        self.cbBasedOnInverts.setObjectName("cbBasedOnInverts")
        self.horizontalLayout_9.addWidget(self.cbBasedOnInverts)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.cbBasedOnContinuity = QtWidgets.QCheckBox(self.PipeDirection)
        self.cbBasedOnContinuity.setObjectName("cbBasedOnContinuity")
        self.horizontalLayout_10.addWidget(self.cbBasedOnContinuity)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        spacerItem14 = QtWidgets.QSpacerItem(20, 450, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem14)
        self.tabWidget.addTab(self.PipeDirection, "")
        self.Continuity = QtWidgets.QWidget()
        self.Continuity.setObjectName("Continuity")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Continuity)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rbContinuity = QtWidgets.QRadioButton(self.Continuity)
        self.rbContinuity.setObjectName("rbContinuity")
        self.verticalLayout_7.addWidget(self.rbContinuity)
        self.label_12 = QtWidgets.QLabel(self.Continuity)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.cbContinuityArea = QtWidgets.QCheckBox(self.Continuity)
        self.cbContinuityArea.setObjectName("cbContinuityArea")
        self.horizontalLayout_11.addWidget(self.cbContinuityArea)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_22 = QtWidgets.QLabel(self.Continuity)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 0, 1, 1, 2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem16, 1, 2, 1, 1)
        self.sbContinuityArea = QtWidgets.QSpinBox(self.Continuity)
        self.sbContinuityArea.setProperty("value", 20)
        self.sbContinuityArea.setObjectName("sbContinuityArea")
        self.gridLayout_7.addWidget(self.sbContinuityArea, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem17, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem18)
        self.cbContinuityInverts = QtWidgets.QCheckBox(self.Continuity)
        self.cbContinuityInverts.setObjectName("cbContinuityInverts")
        self.horizontalLayout_12.addWidget(self.cbContinuityInverts)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem19)
        self.cbContinuityAngle = QtWidgets.QCheckBox(self.Continuity)
        self.cbContinuityAngle.setObjectName("cbContinuityAngle")
        self.horizontalLayout_13.addWidget(self.cbContinuityAngle)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 1, 2, 1, 1)
        self.sbContinuityAngle = QtWidgets.QSpinBox(self.Continuity)
        self.sbContinuityAngle.setMaximum(360)
        self.sbContinuityAngle.setProperty("value", 70)
        self.sbContinuityAngle.setObjectName("sbContinuityAngle")
        self.gridLayout.addWidget(self.sbContinuityAngle, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Continuity)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 2)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem22)
        self.cbContinuityCover = QtWidgets.QCheckBox(self.Continuity)
        self.cbContinuityCover.setObjectName("cbContinuityCover")
        self.horizontalLayout_14.addWidget(self.cbContinuityCover)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem23, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Continuity)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 2)
        self.sbContinuityCover = QtWidgets.QDoubleSpinBox(self.Continuity)
        self.sbContinuityCover.setDecimals(1)
        self.sbContinuityCover.setMaximum(9999999.0)
        self.sbContinuityCover.setProperty("value", 0.5)
        self.sbContinuityCover.setObjectName("sbContinuityCover")
        self.gridLayout_2.addWidget(self.sbContinuityCover, 1, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem24, 1, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        spacerItem25 = QtWidgets.QSpacerItem(20, 286, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem25)
        self.tabWidget.addTab(self.Continuity, "")
        self.FlowTrace = QtWidgets.QWidget()
        self.FlowTrace.setObjectName("FlowTrace")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.FlowTrace)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.rbFlowTrace = QtWidgets.QRadioButton(self.FlowTrace)
        self.rbFlowTrace.setObjectName("rbFlowTrace")
        self.verticalLayout_9.addWidget(self.rbFlowTrace)
        self.label_18 = QtWidgets.QLabel(self.FlowTrace)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem26)
        self.cbFlowTraceArea = QtWidgets.QCheckBox(self.FlowTrace)
        self.cbFlowTraceArea.setObjectName("cbFlowTraceArea")
        self.horizontalLayout_4.addWidget(self.cbFlowTraceArea)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_21 = QtWidgets.QLabel(self.FlowTrace)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 2)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem27, 1, 2, 1, 1)
        self.sbFlowTraceArea = QtWidgets.QSpinBox(self.FlowTrace)
        self.sbFlowTraceArea.setProperty("value", 20)
        self.sbFlowTraceArea.setObjectName("sbFlowTraceArea")
        self.gridLayout_6.addWidget(self.sbFlowTraceArea, 1, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem28, 1, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_6)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem29)
        self.cbFlowTraceInverts = QtWidgets.QCheckBox(self.FlowTrace)
        self.cbFlowTraceInverts.setObjectName("cbFlowTraceInverts")
        self.horizontalLayout_17.addWidget(self.cbFlowTraceInverts)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem30)
        self.cbFlowTraceAngle = QtWidgets.QCheckBox(self.FlowTrace)
        self.cbFlowTraceAngle.setObjectName("cbFlowTraceAngle")
        self.horizontalLayout_15.addWidget(self.cbFlowTraceAngle)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.FlowTrace)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 2)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem31, 1, 2, 1, 1)
        self.sbFlowTraceAngle = QtWidgets.QSpinBox(self.FlowTrace)
        self.sbFlowTraceAngle.setMaximum(360)
        self.sbFlowTraceAngle.setProperty("value", 70)
        self.sbFlowTraceAngle.setObjectName("sbFlowTraceAngle")
        self.gridLayout_3.addWidget(self.sbFlowTraceAngle, 1, 1, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem32, 0, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_3)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem33 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem33)
        self.cbFlowTraceCover = QtWidgets.QCheckBox(self.FlowTrace)
        self.cbFlowTraceCover.setObjectName("cbFlowTraceCover")
        self.horizontalLayout_16.addWidget(self.cbFlowTraceCover)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.FlowTrace)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 2)
        self.sbFlowTraceCover = QtWidgets.QDoubleSpinBox(self.FlowTrace)
        self.sbFlowTraceCover.setPrefix("")
        self.sbFlowTraceCover.setDecimals(1)
        self.sbFlowTraceCover.setMaximum(9999999.0)
        self.sbFlowTraceCover.setProperty("value", 0.5)
        self.sbFlowTraceCover.setObjectName("sbFlowTraceCover")
        self.gridLayout_4.addWidget(self.sbFlowTraceCover, 1, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem34, 0, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem35, 1, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem36)
        self.cbFlowTraceLongPlots = QtWidgets.QCheckBox(self.FlowTrace)
        self.cbFlowTraceLongPlots.setObjectName("cbFlowTraceLongPlots")
        self.horizontalLayout_19.addWidget(self.cbFlowTraceLongPlots)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        spacerItem37 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem37)
        self.tabWidget.addTab(self.FlowTrace, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.runStatus = QtWidgets.QLabel(self.dockWidgetContents)
        self.runStatus.setMinimumSize(QtCore.QSize(300, 0))
        self.runStatus.setObjectName("runStatus")
        self.horizontalLayout_5.addWidget(self.runStatus)
        self.pbRun = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pbRun.setObjectName("pbRun")
        self.horizontalLayout_5.addWidget(self.pbRun)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        IntegrityTool.setWidget(self.dockWidgetContents)

        self.retranslateUi(IntegrityTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IntegrityTool)

    def retranslateUi(self, IntegrityTool):
        _translate = QtCore.QCoreApplication.translate
        IntegrityTool.setWindowTitle(_translate("IntegrityTool", "1D Integrity Tool"))
        self.gbLines.setTitle(_translate("IntegrityTool", "Input Network Lines"))
        self.label.setText(_translate("IntegrityTool", "1D Network Line Layers (1d_nwk_L.shp)"))
        self.browseInputLines.setText(_translate("IntegrityTool", "..."))
        self.btnAddLines.setText(_translate("IntegrityTool", "..."))
        self.btnRemoveLines.setText(_translate("IntegrityTool", "..."))
        self.gbPoints.setTitle(_translate("IntegrityTool", "Input Network Points"))
        self.label_2.setText(_translate("IntegrityTool", "1D Point Layers (1d_nwk_P.shp)"))
        self.browseInputPoints.setText(_translate("IntegrityTool", "..."))
        self.btnAddPoints.setText(_translate("IntegrityTool", "..."))
        self.btnRemovePoints.setText(_translate("IntegrityTool", "..."))
        self.gbTables.setTitle(_translate("IntegrityTool", "Input Tables"))
        self.label_3.setText(_translate("IntegrityTool", "1d Table Layers (1d_tab, 1d_xs, 1d_cs)"))
        self.browseInputTables.setText(_translate("IntegrityTool", "..."))
        self.btnAddTables.setText(_translate("IntegrityTool", "..."))
        self.btnRemoveTables.setText(_translate("IntegrityTool", "..."))
        self.gbDem.setTitle(_translate("IntegrityTool", "Input DEM"))
        self.label_11.setText(_translate("IntegrityTool", "DEM:"))
        self.rbSnapping.setText(_translate("IntegrityTool", "Use Snapping Integrity Check"))
        self.label_5.setText(_translate("IntegrityTool", "<html><head/><body><p>Checks snapping at all input 1D network lines and 1D network points. For lines it will check both the upstream and downstream end of the line are snapped to the upstream or downstream end of another line. If there is no connection point within the user defined exclusion radius it will assume that the line is the most upstream element in the network, or the most downstream, and will not flag an error. For points it wil check that each point is snapped to either an upstream or downstream end of a line. Auto snap will automatically find the closest connection within the radius and snap them together for both lines and points. The tool will output a temporary shp layer and will not edit the input layer.</p></body></html>"))
        self.cbExclRadius.setText(_translate("IntegrityTool", "Use Exclusion Radius When Checking For Snapping"))
        self.label_19.setText(_translate("IntegrityTool", "If there are no other network vertexes within exclusion radius, no snapping error will be produced for current vertex (useful to stop the most upstream or downstream pipe being flagged as \'unsnapped\')"))
        self.label_16.setText(_translate("IntegrityTool", "Exclusion radius (map units)"))
        self.cbAutoSnap.setText(_translate("IntegrityTool", "Auto Snap"))
        self.label_4.setText(_translate("IntegrityTool", "Search radius (map units)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Snapping), _translate("IntegrityTool", "Snapping"))
        self.rbPipeDirection.setText(_translate("IntegrityTool", "Use Pipe Direction Integrity Check"))
        self.label_6.setText(_translate("IntegrityTool", "Checks pipe direction and will correct based on the selected rule(s). Based on inverts will check the gradient of the pipe is in the direction of flow. If there is a negative gradient, the tool will switch the pipe direction. Based on pipe direction continuity will do a basic check on places where the pipe direction does not appear to be continuous. It will ignore pipes that connect to junctions with 3 or more other pipes as these can be ambiguous in determining continuity."))
        self.cbBasedOnInverts.setText(_translate("IntegrityTool", "Based on inverts - will correct if pipe gradient is adverse"))
        self.cbBasedOnContinuity.setText(_translate("IntegrityTool", "Based on pipe direction continuity - will check upstream and downstream pipe directions for continuity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PipeDirection), _translate("IntegrityTool", "Pipe Direction"))
        self.rbContinuity.setText(_translate("IntegrityTool", "Use Continuity Integrity Check"))
        self.label_12.setText(_translate("IntegrityTool", "Will check all 1D inputs for continuity based on the selected options. Check inverts will check both pipe gradient and pipe junctions. Outlet angle convention assumes a straight connection has an angle = 180 deg and anything less than 180 deg has a sharper outlet bend. This tool will output a temporary shape file with all flagged locations. Cross sections snapped to the ends of channels and mid cross sections will be considered."))
        self.cbContinuityArea.setText(_translate("IntegrityTool", "Flow Area Check: check downstream flow area does not decrease"))
        self.label_22.setText(_translate("IntegrityTool", "Where 2 or more pipes enter 1 pipe, flag where there is % decrease greater than: (this is to stop side pipes entering trunk drainage from being flagged - where there is only one pipe entering the downstream pipe this percentage is ignored)"))
        self.sbContinuityArea.setSuffix(_translate("IntegrityTool", "%"))
        self.cbContinuityInverts.setText(_translate("IntegrityTool", "Invert Check: check for adverse gradients and downstream inverts are not higher"))
        self.cbContinuityAngle.setText(_translate("IntegrityTool", "Angle Check: check outflow angles - will not flag side pipes if trunk drain is OK"))
        self.sbContinuityAngle.setSuffix(_translate("IntegrityTool", " deg"))
        self.label_7.setText(_translate("IntegrityTool", "Flag angles less than:"))
        self.cbContinuityCover.setText(_translate("IntegrityTool", "Check Ground Cover"))
        self.label_9.setText(_translate("IntegrityTool", "Flag cover depths less than:"))
        self.sbContinuityCover.setSuffix(_translate("IntegrityTool", " map units"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Continuity), _translate("IntegrityTool", "Continuity"))
        self.rbFlowTrace.setText(_translate("IntegrityTool", "Use Flow Trace Integrity Check"))
        self.label_18.setText(_translate("IntegrityTool", "<html><head/><body><p>Checks the continuity of all upstream pipes from the selected feaures. Similar to the Continuity tool except does not analyse the entire system but rather the upstream flow trace. The tool will output a temporary shape file with all flagged locations as well as creating a selection of flow trace. It also has the additional option of generating a long plot of traced system.</p></body></html>"))
        self.cbFlowTraceArea.setText(_translate("IntegrityTool", "Flow Area Check: check downstream flow area does not decrease"))
        self.label_21.setText(_translate("IntegrityTool", "Where 2 or more pipes enter 1 pipe, flag where there is % decrease greater than: (this is to stop side pipes entering trunk drainage from being flagged - where there is only one pipe entering the downstream pipe this percentage is ignored)"))
        self.sbFlowTraceArea.setSuffix(_translate("IntegrityTool", "%"))
        self.cbFlowTraceInverts.setText(_translate("IntegrityTool", "Invert Check: check for adverse gradients and downstream inverts are not higher"))
        self.cbFlowTraceAngle.setText(_translate("IntegrityTool", "Angle Check: check outflow angles - will not flag side pipes if trunk drain is OK"))
        self.label_14.setText(_translate("IntegrityTool", "Flag outflow angles less than:"))
        self.sbFlowTraceAngle.setSuffix(_translate("IntegrityTool", " deg"))
        self.cbFlowTraceCover.setText(_translate("IntegrityTool", "Cover Check: check pipe obverts against ground elevation"))
        self.label_17.setText(_translate("IntegrityTool", "Flag cover depths less than:"))
        self.sbFlowTraceCover.setSuffix(_translate("IntegrityTool", " map units"))
        self.cbFlowTraceLongPlots.setText(_translate("IntegrityTool", "Generate Long Plots"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FlowTrace), _translate("IntegrityTool", "Flow Trace"))
        self.runStatus.setText(_translate("IntegrityTool", "Ready"))
        self.pbRun.setText(_translate("IntegrityTool", "Run"))

from qgscollapsiblegroupbox import QgsCollapsibleGroupBox