# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proxyui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_proxyDialog(object):
    def setupUi(self, proxyDialog):
        if not proxyDialog.objectName():
            proxyDialog.setObjectName(u"proxyDialog")
        proxyDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        proxyDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(proxyDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.proxyLabel = QLabel(proxyDialog)
        self.proxyLabel.setObjectName(u"proxyLabel")

        self.verticalLayout.addWidget(self.proxyLabel)

        self.proxyText = QTextEdit(proxyDialog)
        self.proxyText.setObjectName(u"proxyText")

        self.verticalLayout.addWidget(self.proxyText)

        self.proxyLabel_2 = QLabel(proxyDialog)
        self.proxyLabel_2.setObjectName(u"proxyLabel_2")

        self.verticalLayout.addWidget(self.proxyLabel_2)

        self.buttonBox = QDialogButtonBox(proxyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(proxyDialog)
        self.buttonBox.accepted.connect(proxyDialog.accept)
        self.buttonBox.rejected.connect(proxyDialog.reject)

        QMetaObject.connectSlotsByName(proxyDialog)
    # setupUi

    def retranslateUi(self, proxyDialog):
        proxyDialog.setWindowTitle(QCoreApplication.translate("proxyDialog", u"Proxy", None))
        self.proxyLabel.setText(QCoreApplication.translate("proxyDialog", u"Paste your SOCKS5 proxy here", None))
        self.proxyText.setPlaceholderText(QCoreApplication.translate("proxyDialog", u"http://user:password@url:port", None))
        self.proxyLabel_2.setText(QCoreApplication.translate("proxyDialog", u"Leave empty if you dont use any", None))
    # retranslateUi

