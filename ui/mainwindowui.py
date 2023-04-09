# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(695, 654)
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.apisComboBox = QComboBox(self.centralwidget)
        self.apisComboBox.setObjectName(u"apisComboBox")

        self.verticalLayout.addWidget(self.apisComboBox)

        self.linkedAccountsTableWidget = QTableWidget(self.centralwidget)
        if (self.linkedAccountsTableWidget.columnCount() < 3):
            self.linkedAccountsTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.linkedAccountsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.linkedAccountsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.linkedAccountsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.linkedAccountsTableWidget.setObjectName(u"linkedAccountsTableWidget")
        self.linkedAccountsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.linkedAccountsTableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.linkedAccountsTableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.followBtn = QPushButton(self.centralwidget)
        self.followBtn.setObjectName(u"followBtn")
        self.followBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.followBtn)

        self.tweetBtn = QPushButton(self.centralwidget)
        self.tweetBtn.setObjectName(u"tweetBtn")
        self.tweetBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.tweetBtn)

        self.retweetBtn = QPushButton(self.centralwidget)
        self.retweetBtn.setObjectName(u"retweetBtn")
        self.retweetBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.retweetBtn)

        self.likeBtn = QPushButton(self.centralwidget)
        self.likeBtn.setObjectName(u"likeBtn")
        self.likeBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.likeBtn)

        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.deleteBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addAPIBtn = QPushButton(self.centralwidget)
        self.addAPIBtn.setObjectName(u"addAPIBtn")

        self.horizontalLayout_2.addWidget(self.addAPIBtn)

        self.linkAccountBtn = QPushButton(self.centralwidget)
        self.linkAccountBtn.setObjectName(u"linkAccountBtn")

        self.horizontalLayout_2.addWidget(self.linkAccountBtn)

        self.importSessionsBtn = QPushButton(self.centralwidget)
        self.importSessionsBtn.setObjectName(u"importSessionsBtn")

        self.horizontalLayout_2.addWidget(self.importSessionsBtn)

        self.exportSessionsBtn = QPushButton(self.centralwidget)
        self.exportSessionsBtn.setObjectName(u"exportSessionsBtn")

        self.horizontalLayout_2.addWidget(self.exportSessionsBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 695, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZeroXTwitter v0 by 0xkitakitsune", None))
        ___qtablewidgetitem = self.linkedAccountsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Account", None));
        ___qtablewidgetitem1 = self.linkedAccountsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Token", None));
        ___qtablewidgetitem2 = self.linkedAccountsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Proxy", None));
        self.followBtn.setText(QCoreApplication.translate("MainWindow", u"Follow", None))
        self.tweetBtn.setText(QCoreApplication.translate("MainWindow", u"Tweet", None))
        self.retweetBtn.setText(QCoreApplication.translate("MainWindow", u"Retweet", None))
        self.likeBtn.setText(QCoreApplication.translate("MainWindow", u"Like", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.addAPIBtn.setText(QCoreApplication.translate("MainWindow", u"Add API", None))
        self.linkAccountBtn.setText(QCoreApplication.translate("MainWindow", u"Link an account", None))
        self.importSessionsBtn.setText(QCoreApplication.translate("MainWindow", u"Import Sessions", None))
        self.exportSessionsBtn.setText(QCoreApplication.translate("MainWindow", u"Export Sessions", None))
    # retranslateUi

