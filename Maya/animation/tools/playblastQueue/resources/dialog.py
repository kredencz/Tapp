# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:/.core/dev/tapp/Tapp/Maya/animation\tools\playblastQueue\resources\dialog.ui'
#
# Created: Mon Aug 15 18:32:32 2016
#      by: Qt UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.width_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.width_spinBox.setMinimum(1)
        self.width_spinBox.setMaximum(999999)
        self.width_spinBox.setProperty("value", 1920)
        self.width_spinBox.setObjectName("width_spinBox")
        self.horizontalLayout.addWidget(self.width_spinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(8, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.height_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.height_spinBox.setMinimum(1)
        self.height_spinBox.setMaximum(999999)
        self.height_spinBox.setProperty("value", 1080)
        self.height_spinBox.setObjectName("height_spinBox")
        self.horizontalLayout.addWidget(self.height_spinBox)
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout.addWidget(self.add_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.export_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.export_pushButton.setObjectName("export_pushButton")
        self.horizontalLayout.addWidget(self.export_pushButton)
        self.import_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.import_pushButton.setObjectName("import_pushButton")
        self.horizontalLayout.addWidget(self.import_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.outputFolder_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputFolder_pushButton.setObjectName("outputFolder_pushButton")
        self.horizontalLayout_2.addWidget(self.outputFolder_pushButton)
        self.outputFolder_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFolder_lineEdit.setObjectName("outputFolder_lineEdit")
        self.horizontalLayout_2.addWidget(self.outputFolder_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.playblastQueue_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.playblastQueue_pushButton.setObjectName("playblastQueue_pushButton")
        self.verticalLayout.addWidget(self.playblastQueue_pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playblast Queue"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "File"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Camera"))
        self.label_2.setText(_translate("MainWindow", "Resolution:"))
        self.label.setText(_translate("MainWindow", "x"))
        self.add_pushButton.setText(_translate("MainWindow", "Add"))
        self.remove_pushButton.setText(_translate("MainWindow", "Remove"))
        self.export_pushButton.setText(_translate("MainWindow", "Export"))
        self.import_pushButton.setText(_translate("MainWindow", "Import"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>If output folder is not specified, the playblasts will be saved in the same folder as each Maya file.</p></body></html>"))
        self.outputFolder_pushButton.setText(_translate("MainWindow", "Output folder:"))
        self.playblastQueue_pushButton.setText(_translate("MainWindow", "Playblast Queue"))

