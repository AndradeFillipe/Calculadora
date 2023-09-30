from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QMainWindow, QLabel)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)