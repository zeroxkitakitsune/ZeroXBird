# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tweetui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_tweetDialog(object):
    def setupUi(self, tweetDialog):
        if not tweetDialog.objectName():
            tweetDialog.setObjectName(u"tweetDialog")
        tweetDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        tweetDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(tweetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tweetLabel = QLabel(tweetDialog)
        self.tweetLabel.setObjectName(u"tweetLabel")

        self.verticalLayout.addWidget(self.tweetLabel)

        self.tweetText = QTextEdit(tweetDialog)
        self.tweetText.setObjectName(u"tweetText")

        self.verticalLayout.addWidget(self.tweetText)

        self.buttonBox = QDialogButtonBox(tweetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(tweetDialog)
        self.buttonBox.accepted.connect(tweetDialog.accept)
        self.buttonBox.rejected.connect(tweetDialog.reject)

        QMetaObject.connectSlotsByName(tweetDialog)
    # setupUi

    def retranslateUi(self, tweetDialog):
        tweetDialog.setWindowTitle(QCoreApplication.translate("tweetDialog", u"Tweet", None))
        self.tweetLabel.setText(QCoreApplication.translate("tweetDialog", u"Enter text to tweet", None))
    # retranslateUi

