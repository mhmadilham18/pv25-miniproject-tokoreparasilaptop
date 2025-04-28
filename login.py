# login.py
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from data.data_pegawai import pegawai


class LoginForm(QWidget):
    def __init__(self, switch_to_dashboard):
        super().__init__()
        self.switch_to_dashboard = switch_to_dashboard
        self.setWindowTitle("Login System")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # === Container untuk isi login ===
        container = QWidget()
        container_layout = QVBoxLayout()
        container.setObjectName("mainContainer")
        container_layout.setAlignment(Qt.AlignCenter)
        container.setLayout(container_layout)
        container.setFixedWidth(550)

        # === Icon Image ===
        # Icon Image
        icon_label = QLabel()
        pixmap = QPixmap("assets/login-icon.png")
        pixmap = pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("""
                    margin-top: 30px;
                """)

        # Heading
        heading = QLabel("Sistem Manajemen Service Computer")
        heading.setAlignment(Qt.AlignCenter)
        heading.setWordWrap(True)
        heading.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: #2C3E50;
            margin-top: 30px;
        """)

        # Subheading
        subheading = QLabel("Silakan login ke Akun Pegawai Anda untuk mengakses dashboard")
        subheading.setAlignment(Qt.AlignCenter)
        subheading.setWordWrap(True)
        subheading.setStyleSheet("""
            font-size: 18px;
            margin-bottom: 30px;
            color: #34495E;
        """)

        # === Username Field ===
        username_label = QLabel("Username")
        username_label.setStyleSheet("""
            font-size: 20px;
            color: #2C3E50;
            font-weight: bold;
            margin-bottom: 5px;
        """)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Masukkan Username Anda")
        self.username_input.setFixedWidth(450)
        self.username_input.setStyleSheet("""
            padding: 16px;
            font-size: 20px;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
        """)

        # === Password Field ===
        password_label = QLabel("Password")
        password_label.setStyleSheet("""
            font-size: 20px;
            color: #2C3E50;
            font-weight: bold;
            margin-bottom: 5px;
        """)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Masukkan Password Anda")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(450)
        self.password_input.setStyleSheet("""
            padding: 16px;
            font-size: 20px;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
        """)

        password_container = QHBoxLayout()
        password_container.addWidget(self.password_input)

        # === Login Button ===
        login_button = QPushButton("Login")
        login_button.setFixedWidth(450)
        login_button.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-bottom: 30px;
            outline: none;
        """)
        login_button.clicked.connect(self.check_login)

        # === Created By Label ===
        created_by_label = QLabel("Created by M. Ilham Abdul Shaleh\nF1D022061")
        created_by_label.setAlignment(Qt.AlignCenter)
        created_by_label.setStyleSheet("""
                font-size: 14px;
                color: #7F8C8D;
                margin-top: 30px;
            """)

        # === Form Layout ===
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addSpacing(10)
        form_layout.addWidget(password_label)
        form_layout.addLayout(password_container)
        form_layout.addSpacing(30)
        form_layout.addWidget(login_button)
        form_layout.setSpacing(15)

        # === Masukkan ke container ===
        container_layout.addWidget(icon_label)
        container_layout.addWidget(heading)
        container_layout.addWidget(subheading)
        container_layout.addSpacing(20)
        container_layout.addLayout(form_layout)
        container_layout.addWidget(created_by_label)  # Add the "Created by" label

        # === Tambahkan container ke main layout ===
        main_layout.addWidget(container)
        # Set StyleSheet untuk container
        self.setStyleSheet("""
                        #mainContainer {
                            background-color: #FFFFFF;
                            border: 2px solid #2980B9;
                            border-radius: 10px;
                            padding: 50px;
                        }

                    """)

        self.setLayout(main_layout)

    def check_login(self):
        """ Fungsi untuk mengecek login """
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # Cek apakah ada field yang kosong
        if not username or not password:
            self.show_message("Input Tidak Lengkap", "Username dan Password tidak boleh kosong", "warning")
            return

        for user in pegawai:
            if user['username'] == username and user['password'] == password:
                self.show_message("Login Berhasil", f"Selamat datang, {user['nama']}!", "success")
                self.switch_to_dashboard(user['nama'])
                return
        self.show_message("Login Gagal", "Pastikan Usernama dan Password yang dimasukkan benar", "error")

    def show_message(self, title, message, status):
        """ Menampilkan QMessageBox untuk notif login """
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QIcon("assets/information.png"))
        msg.setText(message)
        msg.setText(f"""
            <div>
                <h3>{title}</h3>
                <p style="font-size:20px;">{message}</p>
            </div>
        """)

        if status == "success":
            msg.setIcon(QMessageBox.Information)
        elif status == "error":
            msg.setIcon(QMessageBox.Critical)
        elif status == "warning":
            msg.setIcon(QMessageBox.Warning)


        msg.exec_()
