# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retweetui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_retweetDialog(object):
    def setupUi(self, retweetDialog):
        if not retweetDialog.objectName():
            retweetDialog.setObjectName(u"retweetDialog")
        retweetDialog.resize(400, 300)
        retweetDialog.setMinimumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        retweetDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(retweetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.retweetLabel = QLabel(retweetDialog)
        self.retweetLabel.setObjectName(u"retweetLabel")

        self.verticalLayout.addWidget(self.retweetLabel)

        self.rtText = QTextEdit(retweetDialog)
        self.rtText.setObjectName(u"rtText")

        self.verticalLayout.addWidget(self.rtText)

        self.pauseCheckBox = QCheckBox(retweetDialog)
        self.pauseCheckBox.setObjectName(u"pauseCheckBox")

        self.verticalLayout.addWidget(self.pauseCheckBox)

        self.buttonBox = QDialogButtonBox(retweetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(retweetDialog)
        self.buttonBox.accepted.connect(retweetDialog.accept)
        self.buttonBox.rejected.connect(retweetDialog.reject)

        QMetaObject.connectSlotsByName(retweetDialog)
    # setupUi

    def retranslateUi(self, retweetDialog):
        retweetDialog.setWindowTitle(QCoreApplication.translate("retweetDialog", u"Retweet", None))
        self.retweetLabel.setText(QCoreApplication.translate("retweetDialog", u"Paste tweet link to retweet ", None))
        self.pauseCheckBox.setText(QCoreApplication.translate("retweetDialog", u"Add random pause retweets between (1 - 60 seconds) ", None))
    # retranslateUi

