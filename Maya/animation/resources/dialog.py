# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:/.core/dev/tapp/Tapp/Maya/animation/resources/dialog.ui'
#
# Created: Wed Feb 01 16:37:30 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(278, 357)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.central_verticalLayout = QtWidgets.QVBoxLayout()
        self.central_verticalLayout.setObjectName("central_verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zvParentMaster_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.zvParentMaster_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.zvParentMaster_pushButton.setObjectName("zvParentMaster_pushButton")
        self.horizontalLayout.addWidget(self.zvParentMaster_pushButton)
        self.zvChain_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.zvChain_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.zvChain_pushButton.setObjectName("zvChain_pushButton")
        self.horizontalLayout.addWidget(self.zvChain_pushButton)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout.addWidget(self.line_9)
        self.zvParentMasterHelp_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zvParentMasterHelp_pushButton.sizePolicy().hasHeightForWidth())
        self.zvParentMasterHelp_pushButton.setSizePolicy(sizePolicy)
        self.zvParentMasterHelp_pushButton.setMinimumSize(QtCore.QSize(30, 0))
        self.zvParentMasterHelp_pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.zvParentMasterHelp_pushButton.setObjectName("zvParentMasterHelp_pushButton")
        self.horizontalLayout.addWidget(self.zvParentMasterHelp_pushButton)
        self.central_verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.keyCleanUp_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyCleanUp_pushButton.sizePolicy().hasHeightForWidth())
        self.keyCleanUp_pushButton.setSizePolicy(sizePolicy)
        self.keyCleanUp_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.keyCleanUp_pushButton.setObjectName("keyCleanUp_pushButton")
        self.horizontalLayout_17.addWidget(self.keyCleanUp_pushButton)
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.horizontalLayout_17.addWidget(self.line_25)
        self.keyCleanUpHelp_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.keyCleanUpHelp_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyCleanUpHelp_pushButton.sizePolicy().hasHeightForWidth())
        self.keyCleanUpHelp_pushButton.setSizePolicy(sizePolicy)
        self.keyCleanUpHelp_pushButton.setMinimumSize(QtCore.QSize(30, 0))
        self.keyCleanUpHelp_pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.keyCleanUpHelp_pushButton.setObjectName("keyCleanUpHelp_pushButton")
        self.horizontalLayout_17.addWidget(self.keyCleanUpHelp_pushButton)
        self.central_verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.changeRotationOrder_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeRotationOrder_pushButton.sizePolicy().hasHeightForWidth())
        self.changeRotationOrder_pushButton.setSizePolicy(sizePolicy)
        self.changeRotationOrder_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.changeRotationOrder_pushButton.setObjectName("changeRotationOrder_pushButton")
        self.horizontalLayout_21.addWidget(self.changeRotationOrder_pushButton)
        self.changeRotationOrder_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeRotationOrder_comboBox.sizePolicy().hasHeightForWidth())
        self.changeRotationOrder_comboBox.setSizePolicy(sizePolicy)
        self.changeRotationOrder_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.changeRotationOrder_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.changeRotationOrder_comboBox.setObjectName("changeRotationOrder_comboBox")
        self.changeRotationOrder_comboBox.addItem("")
        self.changeRotationOrder_comboBox.addItem("")
        self.changeRotationOrder_comboBox.addItem("")
        self.changeRotationOrder_comboBox.addItem("")
        self.changeRotationOrder_comboBox.addItem("")
        self.changeRotationOrder_comboBox.addItem("")
        self.horizontalLayout_21.addWidget(self.changeRotationOrder_comboBox)
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.horizontalLayout_21.addWidget(self.line_26)
        self.changeRotationOrderHelp_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeRotationOrderHelp_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeRotationOrderHelp_pushButton.sizePolicy().hasHeightForWidth())
        self.changeRotationOrderHelp_pushButton.setSizePolicy(sizePolicy)
        self.changeRotationOrderHelp_pushButton.setMinimumSize(QtCore.QSize(30, 0))
        self.changeRotationOrderHelp_pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.changeRotationOrderHelp_pushButton.setObjectName("changeRotationOrderHelp_pushButton")
        self.horizontalLayout_21.addWidget(self.changeRotationOrderHelp_pushButton)
        self.central_verticalLayout.addLayout(self.horizontalLayout_21)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.localizeImagePlane_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localizeImagePlane_pushButton.sizePolicy().hasHeightForWidth())
        self.localizeImagePlane_pushButton.setSizePolicy(sizePolicy)
        self.localizeImagePlane_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.localizeImagePlane_pushButton.setObjectName("localizeImagePlane_pushButton")
        self.gridLayout.addWidget(self.localizeImagePlane_pushButton, 0, 0, 1, 2)
        self.central_verticalLayout.addLayout(self.gridLayout)
        self.playblastQueue_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.playblastQueue_pushButton.setObjectName("playblastQueue_pushButton")
        self.central_verticalLayout.addWidget(self.playblastQueue_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.central_verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.central_verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tools"))
        self.zvParentMaster_pushButton.setText(_translate("MainWindow", "Zv Parent Master"))
        self.zvChain_pushButton.setText(_translate("MainWindow", "Zv Chain"))
        self.zvParentMasterHelp_pushButton.setText(_translate("MainWindow", "?"))
        self.keyCleanUp_pushButton.setText(_translate("MainWindow", "Key Clean Up"))
        self.keyCleanUpHelp_pushButton.setText(_translate("MainWindow", "?"))
        self.changeRotationOrder_pushButton.setText(_translate("MainWindow", "Change Rotation Order"))
        self.changeRotationOrder_comboBox.setItemText(0, _translate("MainWindow", "xyz"))
        self.changeRotationOrder_comboBox.setItemText(1, _translate("MainWindow", "yzx"))
        self.changeRotationOrder_comboBox.setItemText(2, _translate("MainWindow", "zxy"))
        self.changeRotationOrder_comboBox.setItemText(3, _translate("MainWindow", "xzy"))
        self.changeRotationOrder_comboBox.setItemText(4, _translate("MainWindow", "yxz"))
        self.changeRotationOrder_comboBox.setItemText(5, _translate("MainWindow", "zyx"))
        self.changeRotationOrderHelp_pushButton.setText(_translate("MainWindow", "?"))
        self.localizeImagePlane_pushButton.setText(_translate("MainWindow", "Localize Image Plane"))
        self.playblastQueue_pushButton.setText(_translate("MainWindow", "Playblast Queue"))
