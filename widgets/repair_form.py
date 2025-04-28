# widgets/repair_form.py
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QTextEdit,
                             QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from data.detail_perbaikan import data_perbaikan
from data.data_pegawai import pegawai
from datetime import datetime

class RepairForm(QWidget):
    def __init__(self, update_callback=None):
        super().__init__()
        self.update_callback = update_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Form Title
        form_title = QLabel("Tambah Data Perbaikan")
        form_title.setFont(QFont('Arial', 14, QFont.Bold))
        form_title.setAlignment(Qt.AlignLeft)
        form_title.setStyleSheet("margin-bottom: 10px;")
        main_layout.addWidget(form_title)

        # Form Fields
        fields_layout = QVBoxLayout()

        # Nama Pelanggan
        cust_name_label = QLabel("Nama Pelanggan")
        cust_name_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.cust_name_input = QLineEdit()
        self.cust_name_input.setPlaceholderText("Masukkan nama customer Anda")
        self.cust_name_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(cust_name_label)
        fields_layout.addWidget(self.cust_name_input)

        # Model Device
        model_device_label = QLabel("Model Device")
        model_device_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.model_device_input = QLineEdit()
        self.model_device_input.setPlaceholderText("Masukkan model device customer")
        self.model_device_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(model_device_label)
        fields_layout.addWidget(self.model_device_input)

        # Nama Pegawai
        pegawai_label = QLabel("Nama Pegawai")
        pegawai_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.pegawai_input = QComboBox()
        self.pegawai_input.setStyleSheet(self.input_style())
        for p in pegawai:
            self.pegawai_input.addItem(p["nama"])
        fields_layout.addWidget(pegawai_label)
        fields_layout.addWidget(self.pegawai_input)

        # Keluhan
        keluhan_label = QLabel("Keluhan")
        keluhan_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.keluhan_input = QTextEdit()
        self.keluhan_input.setPlaceholderText("Masukkan keluhan customer")
        self.keluhan_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(keluhan_label)
        fields_layout.addWidget(self.keluhan_input)

        # Detail Perbaikan
        detail_label = QLabel("Detail Perbaikan")
        detail_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.detail_input = QTextEdit()
        self.detail_input.setPlaceholderText("Masukkan detail perbaikan")
        self.detail_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(detail_label)
        fields_layout.addWidget(self.detail_input)

        # Tombol Simpan
        simpan_button = QPushButton("Simpan Data Perbaikan")
        simpan_button.setFixedWidth(450)
        simpan_button.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-top: 20px;
            outline: none;
        """)
        simpan_button.clicked.connect(self.simpan_data)


        button_layout = QHBoxLayout()
        button_layout.addWidget(simpan_button, alignment=Qt.AlignLeft)

        # Susun semua layout
        main_layout.addLayout(fields_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def input_style(self):
        return """
            padding: 12px;
            font-size: 24px;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
        """

    def simpan_data(self):
        nama_pelanggan = self.cust_name_input.text()
        model_device = self.model_device_input.text()
        keluhan = self.keluhan_input.toPlainText()
        detail_perbaikan_text = self.detail_input.toPlainText()
        nama_pegawai = self.pegawai_input.currentText()

        if not nama_pelanggan or not model_device or not keluhan or not detail_perbaikan_text:
            # Show warning message
            msg_box = QMessageBox()
            msg_box.setWindowIcon(QIcon("assets/information.png"))
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Peringatan")
            msg_box.setText(
                """
                <div>
                    <h3>Peringatan</h3>
                    <p style="font-size:20px;">Semua data harus diisi terlebih dahulu</p>
                </div>
                """
            )
            msg_box.exec_()

            return

        # Generate new ID for repair
        new_id = len(data_perbaikan) + 1

        new_repair = {
            "id": new_id,
            "nama_pelanggan": nama_pelanggan,
            "model_laptop": model_device,
            "nama_pegawai": nama_pegawai,
            "keluhan": keluhan,
            "detail_perbaikan": detail_perbaikan_text,
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data_perbaikan.append(new_repair)

        # Clear inputs
        self.cust_name_input.clear()
        self.model_device_input.clear()
        self.keluhan_input.clear()
        self.detail_input.clear()

        # Show success message
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon("assets/information.png"))
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Sukses")
        msg_box.setText(
            f"""
            <div>
                <h3>Sukses</h3>
                <p style="font-size:20px;">Data perbaikan berhasil disimpan dengan ID {new_id}</p>
            </div>
            """
        )
        msg_box.exec_()

        if self.update_callback:
            self.update_callback()
