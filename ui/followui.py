# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'followui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_followDialog(object):
    def setupUi(self, followDialog):
        if not followDialog.objectName():
            followDialog.setObjectName(u"followDialog")
        followDialog.resize(400, 300)
        followDialog.setMinimumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        followDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(followDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.followLabel = QLabel(followDialog)
        self.followLabel.setObjectName(u"followLabel")

        self.verticalLayout.addWidget(self.followLabel)

        self.followText = QTextEdit(followDialog)
        self.followText.setObjectName(u"followText")

        self.verticalLayout.addWidget(self.followText)

        self.buttonBox = QDialogButtonBox(followDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(followDialog)
        self.buttonBox.accepted.connect(followDialog.accept)
        self.buttonBox.rejected.connect(followDialog.reject)

        QMetaObject.connectSlotsByName(followDialog)
    # setupUi

    def retranslateUi(self, followDialog):
        followDialog.setWindowTitle(QCoreApplication.translate("followDialog", u"Follow", None))
        self.followLabel.setText(QCoreApplication.translate("followDialog", u"Enter username to follow here", None))
    # retranslateUi

