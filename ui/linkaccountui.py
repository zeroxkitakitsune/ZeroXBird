# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linkaccountui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_linkAnAccountDialog(object):
    def setupUi(self, linkAnAccountDialog):
        if not linkAnAccountDialog.objectName():
            linkAnAccountDialog.setObjectName(u"linkAnAccountDialog")
        linkAnAccountDialog.resize(400, 300)
        linkAnAccountDialog.setMinimumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(linkAnAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.authorizeLabel = QLabel(linkAnAccountDialog)
        self.authorizeLabel.setObjectName(u"authorizeLabel")

        self.verticalLayout.addWidget(self.authorizeLabel)

        self.authrorizeText = QTextEdit(linkAnAccountDialog)
        self.authrorizeText.setObjectName(u"authrorizeText")

        self.verticalLayout.addWidget(self.authrorizeText)

        self.pinLabel = QLabel(linkAnAccountDialog)
        self.pinLabel.setObjectName(u"pinLabel")

        self.verticalLayout.addWidget(self.pinLabel)

        self.pinText = QTextEdit(linkAnAccountDialog)
        self.pinText.setObjectName(u"pinText")

        self.verticalLayout.addWidget(self.pinText)

        self.buttonBox = QDialogButtonBox(linkAnAccountDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(linkAnAccountDialog)
        self.buttonBox.accepted.connect(linkAnAccountDialog.accept)
        self.buttonBox.rejected.connect(linkAnAccountDialog.reject)

        QMetaObject.connectSlotsByName(linkAnAccountDialog)
    # setupUi

    def retranslateUi(self, linkAnAccountDialog):
        linkAnAccountDialog.setWindowTitle(QCoreApplication.translate("linkAnAccountDialog", u"Link an account", None))
        self.authorizeLabel.setText(QCoreApplication.translate("linkAnAccountDialog", u"Please go here and authorize", None))
        self.pinLabel.setText(QCoreApplication.translate("linkAnAccountDialog", u"Paste the PIN here", None))
    # retranslateUi

