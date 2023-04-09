import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem, QTableView, QMessageBox, QHeaderView
from PySide6.QtCore import QFile, QDir, QPersistentModelIndex

from twitter import Twitter

from ui.mainwindowui import Ui_MainWindow
from ui.apikeysui import Ui_addAPIDialog
from ui.linkaccountui import Ui_linkAnAccountDialog
from ui.followui import Ui_followDialog
from ui.tweetui import Ui_tweetDialog
from ui.retweetui import Ui_retweetDialog
from ui.likeui import Ui_likeDialog
from ui.proxyui import Ui_proxyDialog

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

twitter = {}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.linkedAccountsTableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.ui.linkedAccountsTableWidget.selectionModel().selectionChanged.connect(enableBtns)

class addAPIDialog(QDialog):
    def __init__(self):
        super(addAPIDialog, self).__init__()
        self.ui = Ui_addAPIDialog()
        self.ui.setupUi(self)

class linkAnAccountDialog(QDialog):
    def __init__(self):
        super(linkAnAccountDialog, self).__init__()
        self.ui = Ui_linkAnAccountDialog()
        self.ui.setupUi(self)

class followDialog(QDialog):
    def __init__(self):
        super(followDialog, self).__init__()
        self.ui = Ui_followDialog()
        self.ui.setupUi(self)

class tweetDialog(QDialog):
    def __init__(self):
        super(tweetDialog, self).__init__()
        self.ui = Ui_tweetDialog()
        self.ui.setupUi(self)

class retweetDialog(QDialog):
    def __init__(self):
        super(retweetDialog, self).__init__()
        self.ui = Ui_retweetDialog()
        self.ui.setupUi(self)

class likeDialog(QDialog):
    def __init__(self):
        super(likeDialog, self).__init__()
        self.ui = Ui_likeDialog()
        self.ui.setupUi(self)

class proxyDialog(QDialog):
    def __init__(self):
        super(proxyDialog, self).__init__()
        self.ui = Ui_proxyDialog()
        self.ui.setupUi(self)

def enableBtns(selected, deselected):
    window.ui.followBtn.setEnabled(True)
    window.ui.tweetBtn.setEnabled(True)
    window.ui.retweetBtn.setEnabled(True)
    window.ui.likeBtn.setEnabled(True)
    window.ui.deleteBtn.setEnabled(True)

def addAPI():
    global twitter
    global CONSUMER_KEY
    global CONSUMER_SECRET
    proxy_dialog = proxyDialog()
    proxyBtn = proxy_dialog.exec()
    if proxyBtn == 1:
        proxy = proxy_dialog.ui.proxyText.toPlainText()
        add_api_key_dialog = addAPIDialog()
        button = add_api_key_dialog.exec()
        if button == 1:
            CONSUMER_KEY = add_api_key_dialog.ui.consumerKeyText.toPlainText()
            CONSUMER_SECRET = add_api_key_dialog.ui.consumerSecretText.toPlainText()

            if Twitter.check_api(CONSUMER_KEY, CONSUMER_SECRET, proxy) == True:
                twitter = Twitter(CONSUMER_KEY, CONSUMER_SECRET)
                print("correct")
            else:
                print("false")
            
            window.ui.consumerKeyLabel.setText(f"Consumer Key: {CONSUMER_KEY}")
            window.ui.consumerSecretLabel.setText(f"Consumer Secret: {CONSUMER_SECRET}")
            window.ui.proxyLabel.setText(f"Proxy: {proxy}")

def linkAccount():
    
    global twitter
    
    link_an_account_dialog = linkAnAccountDialog()
    proxy_dialog = proxyDialog()
    proxyBtn = proxy_dialog.exec()
    if proxyBtn == 1:
        proxy = proxy_dialog.ui.proxyText.toPlainText()
        authorization_url = twitter.get_authorize_url(proxy)
        link_an_account_dialog.ui.authrorizeText.insertPlainText(authorization_url)
        button = link_an_account_dialog.exec()
        if button == 1:
            twitter.link_account(link_an_account_dialog.ui.pinText.toPlainText(), proxy)
            window.ui.linkedAccountsTableWidget.setRowCount(len(twitter.listAccounts))
            row = 0
            for account in twitter.listAccounts:
                window.ui.linkedAccountsTableWidget.setItem(row,0,QTableWidgetItem(account['account']))
                window.ui.linkedAccountsTableWidget.setItem(row,1,QTableWidgetItem(account['oauth'].token['oauth_token']))
                window.ui.linkedAccountsTableWidget.setItem(row,2,QTableWidgetItem(account['proxy']))
                row += 1

def importSessions():
    
    global twitter
    
    fileName, _ = QFileDialog.getOpenFileName(window, 'Single File', QDir.rootPath() , '*.json')
    
    twitter.import_sessions(fileName)
    
    window.ui.linkedAccountsTableWidget.setRowCount(len(twitter.listAccounts))
    
    row = 0
    for account in twitter.listAccounts:
        window.ui.linkedAccountsTableWidget.setItem(row,0,QTableWidgetItem(account['account']))
        window.ui.linkedAccountsTableWidget.setItem(row,1,QTableWidgetItem(account['oauth'].token['oauth_token']))
        window.ui.linkedAccountsTableWidget.setItem(row,2,QTableWidgetItem(account['proxy']))
        row += 1

def exportSessions():
    
    global twitter
    
    twitter.export_sessions()

def follow():
    global twitter

    follow_dialog = followDialog()
    
    indexes = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = follow_dialog.exec()
    if button == 1:
        names = []
        for index in indexes:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(index.row(), 0)))
        twitter.follow(names, follow_dialog.ui.followText.toPlainText())

def tweet():
    global twitter
    
    tweet_dialog = tweetDialog()
    
    indexes = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = tweet_dialog.exec()
    if button == 1:
        names = []
        for index in indexes:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(index.row(), 0)))
        twitter.tweet(names, tweet_dialog.ui.tweetText.toPlainText())

def retweet():
    global twitter

    retweet_dialog = retweetDialog()
    
    indexes = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = retweet_dialog.exec()
    if button == 1:
        names = []
        for index in indexes:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(index.row(), 0)))
        twitter.retweet(names, retweet_dialog.ui.rtText.toPlainText())

def like():
    
    global twitter
    
    like_dialog = likeDialog()
    
    indexes = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    button = like_dialog.exec()
    if button == 1:
        names = []
        for index in indexes:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(index.row(), 0)))
        twitter.like(names, like_dialog.ui.likeText.toPlainText())

def delete():
    
    global twitter
    
    indexes = []
    
    names = []
    
    for model_index in window.ui.linkedAccountsTableWidget.selectionModel().selectedRows():
        index = QPersistentModelIndex(model_index)
        indexes.append(index)

    for index in indexes:
        names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(index.row(), 0)))
        window.ui.linkedAccountsTableWidget.removeRow(index.row())
    twitter.delete(names)        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.ui.addAPIBtn.clicked.connect(addAPI)
    window.ui.linkAccountBtn.clicked.connect(linkAccount)
    window.ui.importSessionsBtn.clicked.connect(importSessions)
    window.ui.exportSessionsBtn.clicked.connect(exportSessions)
    window.ui.followBtn.clicked.connect(follow)
    window.ui.tweetBtn.clicked.connect(tweet)
    window.ui.retweetBtn.clicked.connect(retweet)
    window.ui.likeBtn.clicked.connect(like)
    window.ui.deleteBtn.clicked.connect(delete)
    window.show()

    sys.exit(app.exec())


