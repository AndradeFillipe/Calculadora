from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from display import Display
from variables import WINDOW_ICON_PATH
from info import Info
from PySide6.QtGui import QIcon
from botao import Button
from styles import setupTheme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    info = Info("Teste")
    window.addToVLayout(info)
    
    display = Display()
    display.setPlaceholderText('Digite Algo')
    window.addToVLayout(display)

    button = Button('Text')
    window.addToVLayout(button)

    
    app.setWindowIcon(icon)
    window.show()
    
    app.exec()