# detail_transaksi.py
from datetime import datetime

data_transaksi = [
    {
        "id_transaksi": 1,
        "id_perbaikan": 1,
        "total_biaya": 750000,
        "total_uang_dibayar": 800000,
        "kembalian": 50000,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id_transaksi": 2,
        "id_perbaikan": 2,
        "total_biaya": 450000,
        "total_uang_dibayar": 500000,
        "kembalian": 50000,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

]
