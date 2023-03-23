from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('My App')

        # create menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        # toolBar
        toolBar = QToolBar('May toolBar')
        toolBar.setIconSize(QSize(20, 20))
        self.addToolBar(toolBar)
        toolBar.addAction(quit_action)

        action1 = QAction(QIcon('settings.png'), 'Some other action', self)
        action1.setStatusTip('Status message from the action')
        action1.triggered.connect(self.toolBar_button_click)
        toolBar.addAction(action1)

        toolBar.addSeparator()

        button = QPushButton('Click me!')
        toolBar.addWidget(button)

    def quit_app(self):
        self.app.quit()

    def toolBar_button_click(self):
        print('Trigged action')
