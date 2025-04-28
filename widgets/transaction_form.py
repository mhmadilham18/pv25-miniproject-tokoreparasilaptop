# widgets/transaction_form.py
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from data.detail_transaksi import data_transaksi
from datetime import datetime

class TransactionForm(QWidget):
    def __init__(self, update_callback=None):
        super().__init__()
        self.update_callback = update_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()


        # Form Title
        form_title = QLabel("Tambah Data Transaksi")
        form_title.setFont(QFont('Arial', 14, QFont.Bold))
        form_title.setAlignment(Qt.AlignLeft)
        form_title.setStyleSheet("margin-bottom:5px;")

        # Mengatur tinggi tetap untuk form_title
        form_title.setFixedHeight(50)  # Sesuaikan tinggi dengan kebutuhan Anda
        main_layout.addWidget(form_title)

        # Form Fields
        fields_layout = QVBoxLayout()
        fields_layout.setContentsMargins(0, 0, 0, 0)


        # ID Perbaikan
        id_perbaikan_label = QLabel("ID Perbaikan")
        id_perbaikan_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.id_perbaikan = QLineEdit()
        self.id_perbaikan.setPlaceholderText("Masukkan id perbaikan")
        self.id_perbaikan.setStyleSheet(self.input_style())
        fields_layout.addWidget(id_perbaikan_label)
        fields_layout.addWidget(self.id_perbaikan)

        # Total Biaya
        total_biaya_label = QLabel("Total Biaya")
        total_biaya_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.total_biaya_input = QLineEdit()
        self.total_biaya_input.setPlaceholderText("Masukkan total biaya")
        self.total_biaya_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(total_biaya_label)
        fields_layout.addWidget(self.total_biaya_input)
        self.total_biaya_input.textChanged.connect(self.update_kembalian)

        # Total Uang Dibayar
        total_uang_dibayar_label = QLabel("Total Uang Dibayar")
        total_uang_dibayar_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50;")
        self.total_uang_dibayar_input = QLineEdit()
        self.total_uang_dibayar_input.setPlaceholderText("Masukkan total uang yang dibayar")
        self.total_uang_dibayar_input.setStyleSheet(self.input_style())
        fields_layout.addWidget(total_uang_dibayar_label)
        fields_layout.addWidget(self.total_uang_dibayar_input)
        self.total_uang_dibayar_input.textChanged.connect(self.update_kembalian)

        # Kembalian
        kembalian_label = QLabel("Kembalian")
        kembalian_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2C3E50; margin-bottom: 5px;")
        self.kembalian_input = QLineEdit()

        self.kembalian_input.setStyleSheet(self.input_style())
        self.kembalian_input.setReadOnly(True)
        fields_layout.addWidget(kembalian_label)
        fields_layout.addWidget(self.kembalian_input)

        # Tombol Simpan
        simpan_button = QPushButton("Simpan Data Transaksi")
        simpan_button.setFixedWidth(450)
        simpan_button.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-top: 400px;
            outline: none;
        """)
        simpan_button.clicked.connect(self.simpan_data)

        # Membuat tombol di pojok kiri
        button_layout = QHBoxLayout()
        button_layout.addWidget(simpan_button, alignment=Qt.AlignLeft)

        # Susun semua layout
        main_layout.addLayout(fields_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.update_kembalian()

    def input_style(self):
        return """
            padding: 12px;
            font-size: 24px;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
        """

    def simpan_data(self):
        id_perbaikan = self.id_perbaikan.text()
        total_biaya = self.total_biaya_input.text()
        total_uang_dibayar = self.total_uang_dibayar_input.text()
        kembalian = self.kembalian_input.text()

        # Validasi input
        if not total_biaya or not total_uang_dibayar or not kembalian or not id_perbaikan:
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

        try:
            total_biaya = float(total_biaya)
            total_uang_dibayar = float(total_uang_dibayar)
            kembalian = float(kembalian)
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setWindowIcon(QIcon("assets/information.png"))
            msg_box.setIcon(QMessageBox.Error)
            msg_box.setWindowTitle("Peringatan")
            msg_box.setText(
                """
                <div>
                    <h3>Peringatan</h3>
                    <p style="font-size:20px;">Harap masukkan angka yang valid</p>
                </div>
                """
            )
            msg_box.exec_()
            return

        # Generate new ID for transaction
        new_id = len(data_transaksi) + 1

        new_transaction = {
            "id_transaksi": new_id,
            "id_perbaikan": int(id_perbaikan),
            "total_biaya": total_biaya,
            "total_uang_dibayar": total_uang_dibayar,
            "kembalian": kembalian,
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data_transaksi.append(new_transaction)

        # Clear inputs
        self.id_perbaikan.clear()
        self.total_biaya_input.clear()
        self.total_uang_dibayar_input.clear()
        self.kembalian_input.clear()

        # Show success message

        QMessageBox.information(self, "Sukses", f"Data transaksi berhasil disimpan dengan ID {new_id}")

        if self.update_callback:
            self.update_callback()

    def update_kembalian(self):
        """Recalculate change = bayar – biaya setiap kali input berubah."""
        try:
            biaya = float(self.total_biaya_input.text())
            bayar = float(self.total_uang_dibayar_input.text())
            selisih = bayar - biaya
            # Jika bayar < biaya, tampilkan string kosong atau 0
            self.kembalian_input.setText(f"{selisih:.2f}" if selisih >= 0 else "")
        except ValueError:
            # satu atau kedua input belum valid angka
            self.kembalian_input.clear()
