# main.py
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtCore import Qt
from login import LoginForm
from dashboard import Dashboard

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.login_form = LoginForm(self.show_dashboard)
        self.dashboard = None  # Jangan langsung buat, nanti saat login sukses

        self.addWidget(self.login_form)
        self.setCurrentWidget(self.login_form)

        self.setWindowTitle("Aplikasi Pencatatan Pelanggan")
        self.setWindowIcon(QIcon("assets/icon-app.png"))

        self.resizeAndCenter(0.6)  # Misal 60% dari layar

    def resizeAndCenter(self, ratio=0.6):
        screen = self.screen().availableGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        width = int(screen_width * ratio)
        height = int(screen_height * ratio)

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.setGeometry(x, y, width, height)

    def show_dashboard(self, nama_pegawai):
        if self.dashboard is None:
            self.dashboard = Dashboard(nama_pegawai)
            self.addWidget(self.dashboard)

        self.setCurrentWidget(self.dashboard)
        self.resizeAndCenter(0.8)  # Setelah masuk dashboard, misal gedein 80%

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
