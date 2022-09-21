import os.path
import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QColorDialog

try:
    # Only exists on Windows.
    from ctypes import windll

    windll.shell32.SetCurrentProcessExplicitAppUserModelID('com.youssef.color')
except ImportError:
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = QIcon(os.path.join(os.path.dirname(__file__), "color_icon.png"))
    tray_icon = QSystemTrayIcon(icon, app)

    app.setWindowIcon(icon)
    app.setApplicationName("Color picker")
    app.setQuitOnLastWindowClosed(False)

    clipboard = QApplication.clipboard()

    if tray_icon.isSystemTrayAvailable():
        menu = QMenu()

        color_dialog = QColorDialog()

        hex_action = QAction("Hex color")
        hex_action.triggered.connect(
            lambda: (
                color_dialog.exec(),
                clipboard.setText(color_dialog.currentColor().name()),
                tray_icon.showMessage("Color picker", "Copied hex color", icon)
            )
        )

        rgb_action = QAction("RGB color")
        rgb_action.triggered.connect(
            lambda: (
                color_dialog.exec(),
                clipboard.setText(
                    f"rgb({color_dialog.currentColor().red()},"
                    f" {color_dialog.currentColor().green()},"
                    f" {color_dialog.currentColor().blue()})"
                ),
                tray_icon.showMessage("Color picker", "Copied RGB color", icon)
            )
        )

        quit_action = QAction("Quit")
        quit_action.triggered.connect(lambda: sys.exit())

        menu.addAction(hex_action)
        menu.addAction(rgb_action)
        menu.addAction(quit_action)

        tray_icon.setContextMenu(menu)

        tray_icon.setVisible(True)
        tray_icon.setToolTip(app.applicationName())

    sys.exit(app.exec())
