from PySide6.QtWidgets import QLineEdit

class Display(QLineEdit):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 40px')
