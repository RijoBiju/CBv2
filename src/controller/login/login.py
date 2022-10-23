from PySide2.QtWidgets import QMainWindow
from PySide2 import QtCore
from view.login_window import LoginPage
from controller.login import helpers

class LoginGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = LoginPage()
        self.ui.setupUi(self)

        self.setWindowTitle("CB Launcher")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.loginPushButton.clicked.connect(self.user_login)
        self.ui.accountcreationLabel.setText("<a href='https://cbauth.herokuapp.com/registration'>Create an account</a>")
        self.ui.accountcreationLabel.setOpenExternalLinks(True)
        #self.status()

    def user_login(self) -> None:
        username: str = self.ui.usernameLineEdit.text()
        password: str = self.ui.passwordLineEdit.text()
        
        if helpers.login(username, password):
            if self.ui.remembermeCheckBox.isChecked():
                helpers.save_user_details(username, password)
        else:
            self.ui.invaliddetailsPlainTextEdit.setPlainText("Invalid details")

    def setup_statuspage(self) -> None:
        self.ui.loginPushButton.setVisible(False)
        self.ui.skipPushButton.setVisible(False)
        self.ui.usernameLineEdit.setVisible(False)
        self.ui.passwordLineEdit.setVisible(False)
        self.ui.logoLabel.setVisible(False)
        self.ui.remembermeCheckBox.setVisible(False)
        self.ui.accountcreationLabel.setVisible(False)
        self.ui.statusLineEdit.setVisible(True)

    def status(self) -> None:
        self.setup_statuspage()
        self.ui.statusLineEdit.setText("Loading images")