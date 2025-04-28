# detail_perbaikan.py
from datetime import datetime

data_perbaikan = [
    {
        "id": 1,
        "nama_pelanggan": "Rina Agustina",
        "model_laptop": "Asus Vivobook 15",
        "nama_pegawai": "Andi Saputra",
        "keluhan": "Laptop sering mati sendiri",
        "detail_perbaikan": "Ganti baterai dan update BIOS",
        "waktu": "2025-04-25 10:30:00"
    },
    {
        "id": 2,
        "nama_pelanggan": "Doni Pratama",
        "model_laptop": "Acer Aspire 5",
        "nama_pegawai": "Budi Santoso",
        "keluhan": "Keyboard tidak berfungsi",
        "detail_perbaikan": "Ganti keyboard internal",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 3,
        "nama_pelanggan": "Sinta Wulandari",
        "model_laptop": "Lenovo IdeaPad 3",
        "nama_pegawai": "Citra Lestari",
        "keluhan": "Layar bergaris",
        "detail_perbaikan": "Ganti LCD screen",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 4,
        "nama_pelanggan": "Eka Saputra",
        "model_laptop": "HP Pavilion",
        "nama_pegawai": "Andi Saputra",
        "keluhan": "Laptop overheat",
        "detail_perbaikan": "Bersih kipas dan ganti thermal paste",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 5,
        "nama_pelanggan": "Fajar Nugroho",
        "model_laptop": "Dell Inspiron 14",
        "nama_pegawai": "Budi Santoso",
        "keluhan": "Port charger longgar",
        "detail_perbaikan": "Ganti port charger",
        "waktu": "2025-04-25 10:35:00"
    },
    {
        "id": 6,
        "nama_pelanggan": "Gina Permata",
        "model_laptop": "Asus ROG Strix",
        "nama_pegawai": "Citra Lestari",
        "keluhan": "Laptop tidak bisa menyala",
        "detail_perbaikan": "Cek motherboard, ganti IC Power",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 7,
        "nama_pelanggan": "Heri Susanto",
        "model_laptop": "MSI Modern 14",
        "nama_pegawai": "Andi Saputra",
        "keluhan": "Baterai cepat habis",
        "detail_perbaikan": "Ganti baterai baru",
        "waktu": "2025-04-21 10:30:00"
    },
    {
        "id": 8,
        "nama_pelanggan": "Ika Setiawan",
        "model_laptop": "Acer Nitro 5",
        "nama_pegawai": "Budi Santoso",
        "keluhan": "Wifi tidak terdeteksi",
        "detail_perbaikan": "Ganti modul Wifi",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 9,
        "nama_pelanggan": "Joko Rahmat",
        "model_laptop": "MacBook Pro 2019",
        "nama_pegawai": "Citra Lestari",
        "keluhan": "Touchpad tidak berfungsi",
        "detail_perbaikan": "Ganti touchpad flex cable",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 10,
        "nama_pelanggan": "Kiki Amelia",
        "model_laptop": "HP Omen 15",
        "nama_pegawai": "Andi Saputra",
        "keluhan": "Laptop restart sendiri",
        "detail_perbaikan": "Cek RAM, ganti SSD",
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
]
