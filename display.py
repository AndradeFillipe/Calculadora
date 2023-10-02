from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE,DEFAULT_TEXT_MARGIN,MINIMUM_WIDTH
class Display(QLineEdit):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [DEFAULT_TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setMinimumHeight(BIG_FONT_SIZE*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)