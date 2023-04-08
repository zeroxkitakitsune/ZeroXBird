# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'likeui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_likeDialog(object):
    def setupUi(self, likeDialog):
        if not likeDialog.objectName():
            likeDialog.setObjectName(u"likeDialog")
        likeDialog.resize(400, 300)
        likeDialog.setMinimumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        likeDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(likeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(likeDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.likeText = QTextEdit(likeDialog)
        self.likeText.setObjectName(u"likeText")

        self.verticalLayout.addWidget(self.likeText)

        self.buttonBox = QDialogButtonBox(likeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(likeDialog)
        self.buttonBox.accepted.connect(likeDialog.accept)
        self.buttonBox.rejected.connect(likeDialog.reject)

        QMetaObject.connectSlotsByName(likeDialog)
    # setupUi

    def retranslateUi(self, likeDialog):
        likeDialog.setWindowTitle(QCoreApplication.translate("likeDialog", u"Like", None))
        self.label.setText(QCoreApplication.translate("likeDialog", u"Paste tweet link to like", None))
    # retranslateUi

