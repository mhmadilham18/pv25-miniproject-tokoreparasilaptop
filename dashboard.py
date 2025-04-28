# dashboard.py
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QStackedWidget, QTabWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from widgets.cards import CardWidget
from widgets.repair_form import RepairForm
from widgets.transaction_form import TransactionForm
from widgets.data_view import DataViewWidget
from data.detail_perbaikan import data_perbaikan
from data.detail_transaksi import data_transaksi
from datetime import datetime


class Dashboard(QWidget):
    def __init__(self, nama_pegawai=""):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.init_ui()
        self.update_cards()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Header
        header_label = QLabel(f"Selamat Datang, {self.nama_pegawai}!" if self.nama_pegawai else "Selamat Datang!")
        header_label.setAlignment(Qt.AlignLeft)
        header_label.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 36px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-bottom: 10px;
        """)
        main_layout.addWidget(header_label)

        # Cards Area
        self.setup_cards()
        main_layout.addLayout(self.cards_layout)

        # Tab Widget
        tab_widget = QTabWidget()
        tab_widget.tabBar().setFocusPolicy(Qt.NoFocus)

        tab_widget.setStyleSheet("""
            QTabBar::tab {
                background: #ECF0F1;
                font-size: 20px;
                border: 1px solid #BDC3C7;
                border-radius: 5px;
                padding: 16px 16px;
                margin-right: 16px;
                margin-bottom: 30px;
                width: 180px;
                outline: none;
            }
            QTabBar::tab:selected {
                background: #3498DB;
                color: white;
                font-weight: bold;
                outline: none
            }
            QTabBar::tab:hover {
                background: #D6EAF8;
                outline: none;
            }
            
            QTabBar::tab:focus {
                 outline: none;
            }
        """)

        # Create tabs
        repair_form = RepairForm(self.update_cards)
        transaction_form = TransactionForm(self.update_cards)
        data_view = DataViewWidget()

        tab_widget.addTab(repair_form, "Data Perbaikan")
        tab_widget.addTab(transaction_form, "Data Transaksi")
        tab_widget.addTab(data_view, "Lihat Data")

        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def setup_cards(self):
        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(20)

        self.card_hari_ini = CardWidget("Perbaikan Hari Ini", "0", "assets/repair-today.png")
        self.cards_layout.addWidget(self.card_hari_ini)

        self.card_total_perbaikan = CardWidget("Total Semua Perbaikan", "0", "assets/repair-total.png")
        self.cards_layout.addWidget(self.card_total_perbaikan)

        self.card_total_pendapatan = CardWidget("Total Pendapatan", "Rp 0", "assets/income-total.png")
        self.cards_layout.addWidget(self.card_total_pendapatan)

        self.card_pelanggan_baru = CardWidget("Pelanggan Baru Hari Ini", "0", "assets/cust-total.png")
        self.cards_layout.addWidget(self.card_pelanggan_baru)

    def update_cards(self):
        # Get current date in YYYY-MM-DD format
        today = datetime.now().strftime("%Y-%m-%d")

        # Count repairs today
        repairs_today = sum(1 for repair in data_perbaikan if repair["waktu"].startswith(today))

        # Count total repairs
        total_repairs = len(data_perbaikan)

        # Calculate total income
        total_income = sum(trans["total_biaya"] for trans in data_transaksi)

        # Count new customers today (unique names)
        today_customers = set()
        for repair in data_perbaikan:
            if repair["waktu"].startswith(today):
                today_customers.add(repair["nama_pelanggan"])

        new_customers_today = len(today_customers)

        # Update cards
        self.card_hari_ini.update_value(str(repairs_today))
        self.card_total_perbaikan.update_value(str(total_repairs))
        self.card_total_pendapatan.update_value(f"Rp {total_income:,}".replace(",", "."))
        self.card_pelanggan_baru.update_value(str(new_customers_today))