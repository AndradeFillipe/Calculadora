from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from display import Display
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    display = Display()
    display.setPlaceholderText('Digite Algo')
    window.addToVLayout(display)
    app.setWindowIcon(icon)
    window.show()
    
    app.exec()