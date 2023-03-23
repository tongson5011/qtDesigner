from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Widget')
        button1 = QPushButton('Button1')
        button1.clicked.connect(self.button_clicked1)
        button2 = QPushButton('Button2')
        button2.clicked.connect(self.button_clicked2)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def button_clicked1(self):
        print('Button 1 was clicked')

    def button_clicked2(self):
        print('Button 2 was clicked')
