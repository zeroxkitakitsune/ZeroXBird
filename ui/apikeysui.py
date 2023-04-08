# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apikeysui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_addAPIDialog(object):
    def setupUi(self, addAPIDialog):
        if not addAPIDialog.objectName():
            addAPIDialog.setObjectName(u"addAPIDialog")
        addAPIDialog.setEnabled(True)
        addAPIDialog.resize(400, 300)
        addAPIDialog.setMinimumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        addAPIDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(addAPIDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.apiInstructionLabel = QLabel(addAPIDialog)
        self.apiInstructionLabel.setObjectName(u"apiInstructionLabel")

        self.verticalLayout.addWidget(self.apiInstructionLabel)

        self.consumerKeyLabel = QLabel(addAPIDialog)
        self.consumerKeyLabel.setObjectName(u"consumerKeyLabel")

        self.verticalLayout.addWidget(self.consumerKeyLabel)

        self.consumerKeyText = QPlainTextEdit(addAPIDialog)
        self.consumerKeyText.setObjectName(u"consumerKeyText")

        self.verticalLayout.addWidget(self.consumerKeyText)

        self.consumerSecretLabel = QLabel(addAPIDialog)
        self.consumerSecretLabel.setObjectName(u"consumerSecretLabel")

        self.verticalLayout.addWidget(self.consumerSecretLabel)

        self.consumerSecretText = QTextEdit(addAPIDialog)
        self.consumerSecretText.setObjectName(u"consumerSecretText")

        self.verticalLayout.addWidget(self.consumerSecretText)

        self.buttonBox = QDialogButtonBox(addAPIDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(addAPIDialog)
        self.buttonBox.rejected.connect(addAPIDialog.reject)
        self.buttonBox.accepted.connect(addAPIDialog.accept)

        QMetaObject.connectSlotsByName(addAPIDialog)
    # setupUi

    def retranslateUi(self, addAPIDialog):
        addAPIDialog.setWindowTitle(QCoreApplication.translate("addAPIDialog", u"API Keys", None))
        self.apiInstructionLabel.setText(QCoreApplication.translate("addAPIDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Add your API keys here</span></p></body></html>", None))
        self.consumerKeyLabel.setText(QCoreApplication.translate("addAPIDialog", u"Consumer Key", None))
        self.consumerSecretLabel.setText(QCoreApplication.translate("addAPIDialog", u"Consumer Secret", None))
    # retranslateUi

