import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog

class FileDialogWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Select Directory')

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input box
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)

        # Button
        self.btn = QPushButton('Select Directory', self)
        self.btn.clicked.connect(self.openFileDialog)
        layout.addWidget(self.btn)

        self.resize(400, 100)

    def openFileDialog(self):
        # Open file dialog and get the selected directory path
        path = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if path:
            # Set the path in the input box
            self.lineEdit.setText(path)

def main():
    app = QApplication(sys.argv)
    ex = FileDialogWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()