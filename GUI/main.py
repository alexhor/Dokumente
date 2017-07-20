import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QAction)
from editor import Ui_notepad

class StartQT5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_notepad()
        self.ui.setupUi(self)
        # close button
        self.ui.button_close.clicked.connect(self.close)
        # set message buffer
        self.messages = []
        # send button
        self.ui.button_send.clicked.connect(self.send_message)

    def send_message(self):
        self.messages.append(self.ui.message_box.text().strip())
        message_history = '\n'.join(self.messages)
        self.ui.message_history.setPlainText(message_history)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = StartQT5()
    myapp.show()
    sys.exit(app.exec_())
