# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tuflowqgis_check1dIntegrity.ui'
#
# Created: Wed Jun 20 08:50:30 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_check1dIntegrity(object):
    def setupUi(self, check1dIntegrity):
        self.check1dIntegrity = check1dIntegrity
        check1dIntegrity.setObjectName(_fromUtf8("check1dIntegrity"))
        check1dIntegrity.resize(675, 902)
        check1dIntegrity.setFocusPolicy(QtCore.Qt.NoFocus)
        check1dIntegrity.setModal(False)
        self.gridLayout_8 = QtGui.QGridLayout(check1dIntegrity)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.scrollArea = QtGui.QScrollArea(check1dIntegrity)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 655, 882))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taLyrs_lw = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.taLyrs_lw.setEnabled(True)
        self.taLyrs_lw.setMaximumSize(QtCore.QSize(16777215, 75))
        self.taLyrs_lw.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.taLyrs_lw.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.taLyrs_lw.setObjectName(_fromUtf8("taLyrs_lw"))
        self.gridLayout.addWidget(self.taLyrs_lw, 8, 0, 1, 3)
        self.addLine_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.addLine_combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addLine_combo.setObjectName(_fromUtf8("addLine_combo"))
        self.gridLayout.addWidget(self.addLine_combo, 1, 0, 1, 2)
        self.addPoint_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.addPoint_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addPoint_button.setObjectName(_fromUtf8("addPoint_button"))
        self.gridLayout.addWidget(self.addPoint_button, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.removeLine_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.removeLine_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.removeLine_button.setObjectName(_fromUtf8("removeLine_button"))
        self.gridLayout.addWidget(self.removeLine_button, 1, 2, 1, 1)
        self.removePoint_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.removePoint_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.removePoint_button.setObjectName(_fromUtf8("removePoint_button"))
        self.gridLayout.addWidget(self.removePoint_button, 4, 2, 1, 1)
        self.pointLyrs_lw = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.pointLyrs_lw.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pointLyrs_lw.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.pointLyrs_lw.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.pointLyrs_lw.setObjectName(_fromUtf8("pointLyrs_lw"))
        self.gridLayout.addWidget(self.pointLyrs_lw, 5, 0, 1, 3)
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setEnabled(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.addTa_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.addTa_button.setEnabled(True)
        self.addTa_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addTa_button.setObjectName(_fromUtf8("addTa_button"))
        self.gridLayout.addWidget(self.addTa_button, 6, 2, 1, 1)
        self.addPoint_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.addPoint_combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addPoint_combo.setObjectName(_fromUtf8("addPoint_combo"))
        self.gridLayout.addWidget(self.addPoint_combo, 4, 0, 1, 2)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.addLine_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.addLine_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addLine_button.setObjectName(_fromUtf8("addLine_button"))
        self.gridLayout.addWidget(self.addLine_button, 0, 2, 1, 1)
        self.addTa_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.addTa_combo.setEnabled(True)
        self.addTa_combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addTa_combo.setObjectName(_fromUtf8("addTa_combo"))
        self.gridLayout.addWidget(self.addTa_combo, 7, 0, 1, 2)
        self.lineLyrs_lw = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.lineLyrs_lw.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lineLyrs_lw.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.lineLyrs_lw.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lineLyrs_lw.setObjectName(_fromUtf8("lineLyrs_lw"))
        self.gridLayout.addWidget(self.lineLyrs_lw, 2, 0, 1, 3)
        self.removeTa_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.removeTa_button.setEnabled(True)
        self.removeTa_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.removeTa_button.setObjectName(_fromUtf8("removeTa_button"))
        self.gridLayout.addWidget(self.removeTa_button, 7, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.buttonBox = QtGui.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_7.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.outMessBox_cb = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outMessBox_cb.setFont(font)
        self.outMessBox_cb.setObjectName(_fromUtf8("outMessBox_cb"))
        self.gridLayout_6.addWidget(self.outMessBox_cb, 0, 0, 1, 1)
        self.outSel_cb = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outSel_cb.setFont(font)
        self.outSel_cb.setObjectName(_fromUtf8("outSel_cb"))
        self.gridLayout_6.addWidget(self.outSel_cb, 0, 1, 1, 2)
        self.outTxtFile_cb = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outTxtFile_cb.setFont(font)
        self.outTxtFile_cb.setObjectName(_fromUtf8("outTxtFile_cb"))
        self.gridLayout_6.addWidget(self.outTxtFile_cb, 1, 0, 1, 1)
        self.outPLayer_cb = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outPLayer_cb.setFont(font)
        self.outPLayer_cb.setObjectName(_fromUtf8("outPLayer_cb"))
        self.gridLayout_6.addWidget(self.outPLayer_cb, 1, 1, 1, 2)
        self.outFile = QtGui.QLineEdit(self.groupBox_2)
        self.outFile.setEnabled(False)
        self.outFile.setObjectName(_fromUtf8("outFile"))
        self.gridLayout_6.addWidget(self.outFile, 2, 0, 1, 2)
        self.browse_button = QtGui.QPushButton(self.groupBox_2)
        self.browse_button.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.gridLayout_6.addWidget(self.browse_button, 2, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 5, 0, 2, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setChecked(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.correctPipeDir_inverts_cb = QtGui.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.correctPipeDir_inverts_cb.setFont(font)
        self.correctPipeDir_inverts_cb.setText(_fromUtf8(""))
        self.correctPipeDir_inverts_cb.setObjectName(_fromUtf8("correctPipeDir_inverts_cb"))
        self.gridLayout_4.addWidget(self.correctPipeDir_inverts_cb, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)
        self.correctPipeDir_continuity_cb = QtGui.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.correctPipeDir_continuity_cb.setFont(font)
        self.correctPipeDir_continuity_cb.setText(_fromUtf8(""))
        self.correctPipeDir_continuity_cb.setObjectName(_fromUtf8("correctPipeDir_continuity_cb"))
        self.gridLayout_4.addWidget(self.correctPipeDir_continuity_cb, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.autoSnap_cb = QtGui.QCheckBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.autoSnap_cb.setFont(font)
        self.autoSnap_cb.setObjectName(_fromUtf8("autoSnap_cb"))
        self.gridLayout_2.addWidget(self.autoSnap_cb, 1, 0, 1, 1)
        self.check1dPoint_cb = QtGui.QCheckBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.check1dPoint_cb.setFont(font)
        self.check1dPoint_cb.setObjectName(_fromUtf8("check1dPoint_cb"))
        self.gridLayout_2.addWidget(self.check1dPoint_cb, 0, 3, 1, 1)
        self.snapSearchDis_sb = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.snapSearchDis_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.snapSearchDis_sb.setFont(font)
        self.snapSearchDis_sb.setDecimals(4)
        self.snapSearchDis_sb.setMinimum(0.0001)
        self.snapSearchDis_sb.setObjectName(_fromUtf8("snapSearchDis_sb"))
        self.gridLayout_2.addWidget(self.snapSearchDis_sb, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 2)
        self.check1dLine_cb = QtGui.QCheckBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.check1dLine_cb.setFont(font)
        self.check1dLine_cb.setObjectName(_fromUtf8("check1dLine_cb"))
        self.gridLayout_2.addWidget(self.check1dLine_cb, 0, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkArea_cb = QtGui.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkArea_cb.setFont(font)
        self.checkArea_cb.setObjectName(_fromUtf8("checkArea_cb"))
        self.gridLayout_5.addWidget(self.checkArea_cb, 0, 0, 1, 4)
        self.checkGradient_cb = QtGui.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkGradient_cb.setFont(font)
        self.checkGradient_cb.setObjectName(_fromUtf8("checkGradient_cb"))
        self.gridLayout_5.addWidget(self.checkGradient_cb, 1, 0, 1, 4)
        self.checkAngle_cb = QtGui.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkAngle_cb.setFont(font)
        self.checkAngle_cb.setObjectName(_fromUtf8("checkAngle_cb"))
        self.gridLayout_5.addWidget(self.checkAngle_cb, 2, 0, 1, 4)
        self.label_10 = QtGui.QLabel(self.groupBox_7)
        self.label_10.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 4)
        self.angle2_sb = QtGui.QSpinBox(self.groupBox_7)
        self.angle2_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.angle2_sb.setFont(font)
        self.angle2_sb.setMinimum(1)
        self.angle2_sb.setMaximum(360)
        self.angle2_sb.setProperty("value", 90)
        self.angle2_sb.setObjectName(_fromUtf8("angle2_sb"))
        self.gridLayout_5.addWidget(self.angle2_sb, 4, 0, 1, 2)
        self.label_14 = QtGui.QLabel(self.groupBox_7)
        self.label_14.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 4, 2, 1, 2)
        self.checkCover_cb = QtGui.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkCover_cb.setFont(font)
        self.checkCover_cb.setObjectName(_fromUtf8("checkCover_cb"))
        self.gridLayout_5.addWidget(self.checkCover_cb, 5, 0, 1, 4)
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 6, 0, 1, 4)
        self.coverDepth2_sb = QtGui.QDoubleSpinBox(self.groupBox_7)
        self.coverDepth2_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.coverDepth2_sb.setFont(font)
        self.coverDepth2_sb.setDecimals(1)
        self.coverDepth2_sb.setMinimum(-99999.0)
        self.coverDepth2_sb.setMaximum(9999.0)
        self.coverDepth2_sb.setProperty("value", 0.5)
        self.coverDepth2_sb.setObjectName(_fromUtf8("coverDepth2_sb"))
        self.gridLayout_5.addWidget(self.coverDepth2_sb, 7, 0, 1, 3)
        self.label_13 = QtGui.QLabel(self.groupBox_7)
        self.label_13.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 7, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_7)
        self.label_12.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 8, 0, 1, 1)
        self.dem_combo_2 = QtGui.QComboBox(self.groupBox_7)
        self.dem_combo_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dem_combo_2.setFont(font)
        self.dem_combo_2.setObjectName(_fromUtf8("dem_combo_2"))
        self.gridLayout_5.addWidget(self.dem_combo_2, 8, 1, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 6, 2, 1, 1)
        self.name1d_combo = QtGui.QComboBox(self.groupBox_3)
        self.name1d_combo.setEnabled(False)
        self.name1d_combo.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name1d_combo.setFont(font)
        self.name1d_combo.setObjectName(_fromUtf8("name1d_combo"))
        self.gridLayout_3.addWidget(self.name1d_combo, 4, 0, 1, 3)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 3)
        self.removeStartNwk_button = QtGui.QPushButton(self.groupBox_3)
        self.removeStartNwk_button.setEnabled(False)
        self.removeStartNwk_button.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removeStartNwk_button.setFont(font)
        self.removeStartNwk_button.setObjectName(_fromUtf8("removeStartNwk_button"))
        self.gridLayout_3.addWidget(self.removeStartNwk_button, 4, 4, 1, 1)
        self.coverDepth_sb = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.coverDepth_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.coverDepth_sb.setFont(font)
        self.coverDepth_sb.setDecimals(1)
        self.coverDepth_sb.setMinimum(-99999.0)
        self.coverDepth_sb.setMaximum(9999.0)
        self.coverDepth_sb.setProperty("value", 0.5)
        self.coverDepth_sb.setObjectName(_fromUtf8("coverDepth_sb"))
        self.gridLayout_3.addWidget(self.coverDepth_sb, 6, 3, 1, 1)
        self.startNwk_lw = QtGui.QListWidget(self.groupBox_3)
        self.startNwk_lw.setEnabled(False)
        self.startNwk_lw.setMaximumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.startNwk_lw.setFont(font)
        self.startNwk_lw.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.startNwk_lw.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.startNwk_lw.setObjectName(_fromUtf8("startNwk_lw"))
        self.gridLayout_3.addWidget(self.startNwk_lw, 5, 0, 1, 7)
        self.getGroundElev_cb = QtGui.QCheckBox(self.groupBox_3)
        self.getGroundElev_cb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.getGroundElev_cb.setFont(font)
        self.getGroundElev_cb.setObjectName(_fromUtf8("getGroundElev_cb"))
        self.gridLayout_3.addWidget(self.getGroundElev_cb, 6, 0, 1, 2)
        self.angle_sb = QtGui.QSpinBox(self.groupBox_3)
        self.angle_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.angle_sb.setFont(font)
        self.angle_sb.setMinimum(1)
        self.angle_sb.setMaximum(360)
        self.angle_sb.setProperty("value", 90)
        self.angle_sb.setObjectName(_fromUtf8("angle_sb"))
        self.gridLayout_3.addWidget(self.angle_sb, 0, 3, 1, 1)
        self.plotDsConn_cb = QtGui.QCheckBox(self.groupBox_3)
        self.plotDsConn_cb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plotDsConn_cb.setFont(font)
        self.plotDsConn_cb.setObjectName(_fromUtf8("plotDsConn_cb"))
        self.gridLayout_3.addWidget(self.plotDsConn_cb, 13, 0, 1, 2)
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 0, 4, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 6, 4, 1, 1)
        self.addStartNwk_button = QtGui.QPushButton(self.groupBox_3)
        self.addStartNwk_button.setEnabled(False)
        self.addStartNwk_button.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addStartNwk_button.setFont(font)
        self.addStartNwk_button.setObjectName(_fromUtf8("addStartNwk_button"))
        self.gridLayout_3.addWidget(self.addStartNwk_button, 4, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 3)
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 11, 0, 1, 1)
        self.dem_combo = QtGui.QComboBox(self.groupBox_3)
        self.dem_combo.setEnabled(False)
        self.dem_combo.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dem_combo.setFont(font)
        self.dem_combo.setObjectName(_fromUtf8("dem_combo"))
        self.gridLayout_3.addWidget(self.dem_combo, 11, 1, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(3, 1)
        self.gridLayout_7.setRowStretch(4, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(check1dIntegrity)
        self.buttonBox.rejected.connect(check1dIntegrity.reject)
        QtCore.QMetaObject.connectSlotsByName(check1dIntegrity)

    def retranslateUi(self, check1dIntegrity):
        check1dIntegrity.setWindowTitle(_translate("check1dIntegrity", "Check 1D Network Integrity", None))
        self.addPoint_button.setText(_translate("check1dIntegrity", "Add", None))
        self.label_2.setText(_translate("check1dIntegrity", "1D network Point Layer", None))
        self.removeLine_button.setText(_translate("check1dIntegrity", "Remove", None))
        self.removePoint_button.setText(_translate("check1dIntegrity", "Remove", None))
        self.label_8.setText(_translate("check1dIntegrity", "1D Table Layer", None))
        self.addTa_button.setText(_translate("check1dIntegrity", "Add", None))
        self.label.setText(_translate("check1dIntegrity", "1D network Line Layer", None))
        self.addLine_button.setText(_translate("check1dIntegrity", "Add", None))
        self.removeTa_button.setText(_translate("check1dIntegrity", "Remove", None))
        self.groupBox_2.setTitle(_translate("check1dIntegrity", "Output Options", None))
        self.outMessBox_cb.setText(_translate("check1dIntegrity", "Output to message box", None))
        self.outSel_cb.setText(_translate("check1dIntegrity", "Output as selection", None))
        self.outTxtFile_cb.setText(_translate("check1dIntegrity", "Output to txt file", None))
        self.outPLayer_cb.setText(_translate("check1dIntegrity", "Output to 1D_integrity_check.shp", None))
        self.browse_button.setText(_translate("check1dIntegrity", "Browse", None))
        self.groupBox_6.setTitle(_translate("check1dIntegrity", "Correct Pipe Direction", None))
        self.label_5.setText(_translate("check1dIntegrity", "Based on inverts - will correct if pipe gradient is adverse", None))
        self.label_6.setText(_translate("check1dIntegrity", "Based on pipe direction continuity - will check upstream and downstream pipe directions for continuity", None))
        self.groupBox_4.setTitle(_translate("check1dIntegrity", "Snapping", None))
        self.autoSnap_cb.setText(_translate("check1dIntegrity", "Auto Snap", None))
        self.check1dPoint_cb.setText(_translate("check1dIntegrity", "Check 1D Point-Line snapping", None))
        self.label_4.setText(_translate("check1dIntegrity", "Search radius (map units)", None))
        self.check1dLine_cb.setText(_translate("check1dIntegrity", "Check 1D Line-Line snapping", None))
        self.groupBox_7.setTitle(_translate("check1dIntegrity", "Continuity Check", None))
        self.checkArea_cb.setText(_translate("check1dIntegrity", "Check downstream area", None))
        self.checkGradient_cb.setText(_translate("check1dIntegrity", "Check inverts", None))
        self.checkAngle_cb.setText(_translate("check1dIntegrity", "Check outlet angle", None))
        self.label_10.setText(_translate("check1dIntegrity", "Flag angles less than:", None))
        self.label_14.setText(_translate("check1dIntegrity", "degrees", None))
        self.checkCover_cb.setText(_translate("check1dIntegrity", "Check cover", None))
        self.label_11.setText(_translate("check1dIntegrity", "Flag depths less than:", None))
        self.label_13.setText(_translate("check1dIntegrity", "map units", None))
        self.label_12.setText(_translate("check1dIntegrity", "DEM", None))
        self.groupBox_3.setTitle(_translate("check1dIntegrity", "Flow Trace (Upstream to Downstream)", None))
        self.label_16.setText(_translate("check1dIntegrity", "Flag depths less than:", None))
        self.label_3.setText(_translate("check1dIntegrity", "Starting at elements:", None))
        self.removeStartNwk_button.setText(_translate("check1dIntegrity", "Remove", None))
        self.getGroundElev_cb.setText(_translate("check1dIntegrity", "Get ground elevations", None))
        self.plotDsConn_cb.setText(_translate("check1dIntegrity", "Plot output in TUPLOT", None))
        self.label_18.setText(_translate("check1dIntegrity", "degrees", None))
        self.label_17.setText(_translate("check1dIntegrity", "map units", None))
        self.addStartNwk_button.setText(_translate("check1dIntegrity", "Add", None))
        self.label_9.setText(_translate("check1dIntegrity", "Flag Network Connection Angles less than:", None))
        self.label_15.setText(_translate("check1dIntegrity", "DEM", None))
