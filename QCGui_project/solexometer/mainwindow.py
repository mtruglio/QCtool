# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mtruglio/Desktop/Solexometer/QCGui_project/solexometer/QC_main/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(780, 830)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(780, 830))
        MainWindow.setMaximumSize(QtCore.QSize(780, 850))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 761, 791))
        self.tabWidget.setStyleSheet(_fromUtf8("background: rgb(235, 235, 235);\n"
"font: 10pt \"Sans Serif\";"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.runs_tab = QtGui.QWidget()
        self.runs_tab.setObjectName(_fromUtf8("runs_tab"))
        self.new_table = QtGui.QTableWidget(self.runs_tab)
        self.new_table.setGeometry(QtCore.QRect(30, 40, 700, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_table.sizePolicy().hasHeightForWidth())
        self.new_table.setSizePolicy(sizePolicy)
        self.new_table.setMinimumSize(QtCore.QSize(700, 150))
        self.new_table.setMaximumSize(QtCore.QSize(700, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_table.setFont(font)
        self.new_table.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.new_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.new_table.setAlternatingRowColors(True)
        self.new_table.setObjectName(_fromUtf8("new_table"))
        self.new_table.setColumnCount(5)
        self.new_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.new_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.new_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.new_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.new_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.new_table.setHorizontalHeaderItem(4, item)
        self.new_table.horizontalHeader().setCascadingSectionResizes(False)
        self.new_table.horizontalHeader().setDefaultSectionSize(300)
        self.new_table.horizontalHeader().setMinimumSectionSize(20)
        self.new_table.horizontalHeader().setSortIndicatorShown(False)
        self.new_table.horizontalHeader().setStretchLastSection(True)
        self.new_table.verticalHeader().setVisible(False)
        self.new_table.verticalHeader().setDefaultSectionSize(30)
        self.completed_table = QtGui.QTableWidget(self.runs_tab)
        self.completed_table.setGeometry(QtCore.QRect(30, 510, 700, 241))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.completed_table.sizePolicy().hasHeightForWidth())
        self.completed_table.setSizePolicy(sizePolicy)
        self.completed_table.setMinimumSize(QtCore.QSize(700, 150))
        self.completed_table.setMaximumSize(QtCore.QSize(700, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.completed_table.setFont(font)
        self.completed_table.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.completed_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.completed_table.setAlternatingRowColors(True)
        self.completed_table.setObjectName(_fromUtf8("completed_table"))
        self.completed_table.setColumnCount(6)
        self.completed_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.completed_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.completed_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.completed_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.completed_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.completed_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.completed_table.setHorizontalHeaderItem(5, item)
        self.completed_table.horizontalHeader().setDefaultSectionSize(390)
        self.completed_table.horizontalHeader().setMinimumSectionSize(23)
        self.completed_table.horizontalHeader().setSortIndicatorShown(False)
        self.completed_table.horizontalHeader().setStretchLastSection(True)
        self.completed_table.verticalHeader().setVisible(False)
        self.completed_table.verticalHeader().setDefaultSectionSize(30)
        self.running_table = QtGui.QTableWidget(self.runs_tab)
        self.running_table.setGeometry(QtCore.QRect(30, 320, 700, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.running_table.sizePolicy().hasHeightForWidth())
        self.running_table.setSizePolicy(sizePolicy)
        self.running_table.setMinimumSize(QtCore.QSize(700, 150))
        self.running_table.setMaximumSize(QtCore.QSize(700, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.running_table.setFont(font)
        self.running_table.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.running_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.running_table.setAlternatingRowColors(True)
        self.running_table.setObjectName(_fromUtf8("running_table"))
        self.running_table.setColumnCount(6)
        self.running_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.running_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.running_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.running_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.running_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(5, item)
        self.running_table.horizontalHeader().setDefaultSectionSize(390)
        self.running_table.horizontalHeader().setMinimumSectionSize(23)
        self.running_table.horizontalHeader().setSortIndicatorShown(False)
        self.running_table.horizontalHeader().setStretchLastSection(True)
        self.running_table.verticalHeader().setVisible(False)
        self.running_table.verticalHeader().setDefaultSectionSize(30)
        self.running_table.verticalHeader().setSortIndicatorShown(False)
        self.label = QtGui.QLabel(self.runs_tab)
        self.label.setGeometry(QtCore.QRect(67, 10, 161, 21))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.runs_tab)
        self.label_2.setGeometry(QtCore.QRect(36, 10, 21, 21))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/redlight.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.runs_tab)
        self.label_3.setGeometry(QtCore.QRect(65, 290, 161, 21))
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.runs_tab)
        self.label_4.setGeometry(QtCore.QRect(35, 290, 21, 21))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icons/yellowlight.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.runs_tab)
        self.label_5.setGeometry(QtCore.QRect(66, 480, 161, 21))
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.runs_tab)
        self.label_6.setGeometry(QtCore.QRect(35, 480, 21, 21))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icons/greenlight.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.RawFolder = QtGui.QLineEdit(self.runs_tab)
        self.RawFolder.setGeometry(QtCore.QRect(210, 10, 401, 22))
        self.RawFolder.setReadOnly(True)
        self.RawFolder.setObjectName(_fromUtf8("RawFolder"))
        self.RawBrowse = QtGui.QPushButton(self.runs_tab)
        self.RawBrowse.setGeometry(QtCore.QRect(630, 9, 80, 24))
        self.RawBrowse.setObjectName(_fromUtf8("RawBrowse"))
        self.CompletedFolder = QtGui.QLineEdit(self.runs_tab)
        self.CompletedFolder.setGeometry(QtCore.QRect(210, 480, 401, 22))
        self.CompletedFolder.setReadOnly(True)
        self.CompletedFolder.setObjectName(_fromUtf8("CompletedFolder"))
        self.CompletedBrowse = QtGui.QPushButton(self.runs_tab)
        self.CompletedBrowse.setGeometry(QtCore.QRect(630, 479, 80, 24))
        self.CompletedBrowse.setObjectName(_fromUtf8("CompletedBrowse"))
        self.tabWidget.addTab(self.runs_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 780, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QC-o-meter", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Runs</p></body></html>", None))
        item = self.new_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder name", None))
        item = self.new_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project", None))
        item = self.new_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Client", None))
        item = self.new_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sequenced", None))
        item = self.new_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Action", None))
        item = self.completed_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder name", None))
        item = self.completed_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project", None))
        item = self.completed_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Client", None))
        item = self.completed_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Completed", None))
        item = self.running_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder name", None))
        item = self.running_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project", None))
        item = self.running_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Started", None))
        item = self.running_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "JobID", None))
        item = self.running_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Unprocessed runs</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Processing</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Completed</span></p></body></html>", None))
        self.RawBrowse.setText(_translate("MainWindow", "Browse...", None))
        self.CompletedBrowse.setText(_translate("MainWindow", "Browse...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.runs_tab), _translate("MainWindow", "Runs", None))

