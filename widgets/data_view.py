# widgets/data_view.py
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QTabWidget, QTableWidget, QTableWidgetItem, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from data.detail_perbaikan import data_perbaikan
from data.detail_transaksi import data_transaksi
from PyQt5.QtWidgets import QHeaderView, QStyledItemDelegate



class DataViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create nested tabs for repair and transaction data
        data_tabs = QTabWidget()
        data_tabs.tabBar().setFocusPolicy(Qt.NoFocus)

        # Repair Data Tab
        repair_data_widget = QWidget()
        repair_layout = QVBoxLayout()

        repair_header = QHBoxLayout()
        repair_title = QLabel("Data Perbaikan")
        repair_title.setFont(QFont('Arial', 16, QFont.Bold))
        repair_header.addWidget(repair_title)

        refresh_repair_btn = QPushButton("Refresh")
        refresh_repair_btn.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-bottom: 30px;
            outline: none;
        """)
        refresh_repair_btn.clicked.connect(self.refresh_repair_data)
        repair_header.addWidget(refresh_repair_btn, alignment=Qt.AlignRight)

        repair_layout.addLayout(repair_header)

        self.repair_table = QTableWidget()
        self.repair_table.setColumnCount(7)
        self.repair_table.setHorizontalHeaderLabels([
            "ID", "Nama Pelanggan", "Model Laptop", "Pegawai",
            "Keluhan", "Detail Perbaikan", "Waktu"
        ])
        self.repair_table.setWordWrap(True)
        self.repair_table.setItemDelegate(QStyledItemDelegate(self.repair_table))
        hdr = self.repair_table.horizontalHeader()
        for i in (0, 1, 2, 3, 6):
            hdr.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        for i in (4, 5):
            hdr.setSectionResizeMode(i, QHeaderView.Stretch)

        repair_layout.addWidget(self.repair_table)
        repair_data_widget.setLayout(repair_layout)

        # Transaction Data Tab
        transaction_data_widget = QWidget()
        transaction_layout = QVBoxLayout()

        trans_header = QHBoxLayout()
        transaction_title = QLabel("Data Transaksi")
        transaction_title.setFont(QFont('Arial', 16, QFont.Bold))
        trans_header.addWidget(transaction_title)

        refresh_trans_btn = QPushButton("Refresh")
        refresh_trans_btn.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 16px;
            border-radius: 5px;
            margin-bottom: 30px;
            outline: none;
        """)
        refresh_trans_btn.clicked.connect(self.refresh_transaction_data)
        trans_header.addWidget(refresh_trans_btn, alignment=Qt.AlignRight)

        transaction_layout.addLayout(trans_header)

        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(5)
        self.transaction_table.setHorizontalHeaderLabels([
            "ID Perbaikan", "Total Biaya", "Total Dibayar", "Kembalian", "Waktu"
        ])
        self.transaction_table.setWordWrap(True)
        self.transaction_table.setItemDelegate(QStyledItemDelegate(self.transaction_table))
        hdr2 = self.transaction_table.horizontalHeader()
        for i in (0, 4):
            hdr2.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        for i in (1, 2, 3):
            hdr2.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        transaction_layout.addWidget(self.transaction_table)
        transaction_data_widget.setLayout(transaction_layout)

        # Add tabs
        data_tabs.addTab(repair_data_widget, "Data Perbaikan")
        data_tabs.addTab(transaction_data_widget, "Data Transaksi")

        layout.addWidget(data_tabs)
        self.setLayout(layout)

        # Load initial data
        self.refresh_repair_data()
        self.refresh_transaction_data()



    def refresh_repair_data(self):
        self.repair_table.setRowCount(0)  # Clear existing rows


        # Add each item from data_perbaikan to the table
        for row, repair in enumerate(data_perbaikan):
            self.repair_table.insertRow(row)
            self.repair_table.setItem(row, 0, QTableWidgetItem(str(repair["id"])))
            self.repair_table.setItem(row, 1, QTableWidgetItem(repair["nama_pelanggan"]))
            self.repair_table.setItem(row, 2, QTableWidgetItem(repair["model_laptop"]))
            self.repair_table.setItem(row, 3, QTableWidgetItem(repair["nama_pegawai"]))
            self.repair_table.setItem(row, 4, QTableWidgetItem(repair["keluhan"]))
            self.repair_table.setItem(row, 5, QTableWidgetItem(repair["detail_perbaikan"]))
            self.repair_table.setItem(row, 6, QTableWidgetItem(repair["waktu"]))
        self.repair_table.resizeRowsToContents()

    def refresh_transaction_data(self):
        self.transaction_table.setRowCount(0)  # Clear existing rows

        # Add each item from data_transaksi to the table
        for row, trans in enumerate(data_transaksi):
            self.transaction_table.insertRow(row)
            self.transaction_table.setItem(row, 0, QTableWidgetItem(str(trans["id_perbaikan"])))
            self.transaction_table.setItem(row, 1, QTableWidgetItem(f"Rp {trans['total_biaya']:,}".replace(",", ".")))
            self.transaction_table.setItem(row, 2,
                                           QTableWidgetItem(f"Rp {trans['total_uang_dibayar']:,}".replace(",", ".")))
            self.transaction_table.setItem(row, 3, QTableWidgetItem(f"Rp {trans['kembalian']:,}".replace(",", ".")))
            self.transaction_table.setItem(row, 4, QTableWidgetItem(trans["waktu"]))
        self.transaction_table.resizeRowsToContents()