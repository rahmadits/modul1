from tabulate import tabulate

gudang = {
    "BA001": {"nama": "Laptop", "merk": "Dell", "jumlah": 10, "harga": 9500000},
    "BA002": {"nama": "Printer", "merk": "HP", "jumlah": 15, "harga": 2100000},
    "BA003": {"nama": "Smartphone", "merk": "Samsung", "jumlah": 50, "harga": 20000},
    "BA004": {"nama": "Tablet", "merk": "Apple", "jumlah": 40, "harga": 13500000},
    "BA005": {"nama": "Monitor", "merk": "LG", "jumlah": 8, "harga": 1200000},
    "BA006": {"nama": "Kulkas", "merk": "SHARP", "jumlah": 35, "harga": 3200000},
    "BA007": {"nama": "Televisi", "merk": "Sony", "jumlah": 20, "harga": 6000000},
    "BA008": {"nama": "AC", "merk": "Daikin", "jumlah": 25, "harga": 2500000},
    "BA009": {"nama": "Mesin Cuci", "merk": "AQUA", "jumlah": 10, "harga": 4000000},
    "BA010": {"nama": "Speaker", "merk": "JBL", "jumlah": 45, "harga": 9000000}
}

# tambah
def tambah_barang():
    while True:
        kode_barang = input("Masukkan kode barang (format BAxxx): ")
        if len(kode_barang) == 5 and kode_barang.startswith("BA") and kode_barang[2:].isdigit():
            break
        else:
            print("Format kode barang tidak valid. Gunakan format BAxxx (misal: BA001).")

    nama_barang = input("Masukkan nama barang: ")
    merk_barang = input("Masukkan merk barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    harga_barang = float(input("Masukkan harga barang: "))

    barang = {
        'nama': nama_barang,
        'merk': merk_barang,
        'jumlah': jumlah_barang,
        'harga': harga_barang
    }

    gudang[kode_barang] = barang
    print(f"Barang {nama_barang} berhasil ditambahkan ke gudang!")

# Fungsi untuk menampilkan daftar barang di gudang
def tampilkan_barang():
    if not gudang:
        print("Gudang kosong. Tidak ada barang yang tersedia.")
        return

    data_barang = []
    for kode, barang in gudang.items():
        data_barang.append([kode, barang['nama'], barang['merk'], barang['jumlah'], barang['harga']])

    print("\nDaftar Barang di Gudang:")
    table_headers = ["Kode Barang", "Nama Barang", "Merk Barang", "Jumlah Barang", "Harga Barang"]
    print(tabulate(data_barang, headers=table_headers, tablefmt="grid"))

# menampilkan barang berdasarkan kode
def tampilkan_barang_berdasarkan_kode(kode):
    if kode in gudang:
        data_barang = [[kode, gudang[kode]['nama'], gudang[kode]['merk'], gudang[kode]['jumlah'], gudang[kode]['harga']]]
        table_headers = ["Kode Barang", "Nama Barang", "Merk Barang", "Jumlah Barang", "Harga Barang"]
        print("\nBarang dengan Kode Barang", kode)
        print(tabulate(data_barang, headers=table_headers, tablefmt="grid"))
    else:
        print(f"Tidak ada barang dengan Kode Barang {kode} di gudang.")

# menampilkan
def tampilkan_barang():
    if not gudang:
        print("Gudang kosong. Tidak ada barang yang tersedia.")
    else:
        data_barang = []
        for kode, barang in gudang.items():
            data_barang.append([kode, barang['nama'], barang['merk'], barang['jumlah'], barang['harga']])

        print("\nDaftar Barang di Gudang:")
        table_headers = ["Kode Barang", "Nama Barang", "Merk Barang", "Jumlah Barang", "Harga Barang"]
        print(tabulate(data_barang, headers=table_headers, tablefmt="grid"))

# Ubah
def ubah_barang():
    if not gudang:
        print("Gudang kosong. Tidak ada barang yang tersedia.")
        return

    while True:
        kode_barang = input("Masukkan kode barang yang akan diubah: ")
        if kode_barang in gudang:
            break
        else:
            print("Kode barang tidak ditemukan. Masukkan kode yang benar.")

    print(f"Data Barang sebelum diubah:")
    tampilkan_barang()

    nama_barang = input("Masukkan nama barang baru (kosongkan jika tidak ingin mengubah): ")
    merk_barang = input("Masukkan merk barang baru (kosongkan jika tidak ingin mengubah): ")
    jumlah_barang = input("Masukkan jumlah barang baru (kosongkan jika tidak ingin mengubah): ")
    harga_barang = input("Masukkan harga barang baru (kosongkan jika tidak ingin mengubah): ")

    if nama_barang:
        gudang[kode_barang]['nama'] = nama_barang
    if merk_barang:
        gudang[kode_barang]['merk'] = merk_barang
    if jumlah_barang:
        try:
            gudang[kode_barang]['jumlah'] = int(jumlah_barang)
        except ValueError:
            print("Jumlah barang harus berupa angka. Pengubahan dibatalkan.")
    if harga_barang:
        try:
            gudang[kode_barang]['harga'] = float(harga_barang)
        except ValueError:
            print("Harga barang harus berupa angka. Pengubahan dibatalkan.")

    print(f"Data Barang berhasil diubah!")
    print(f"Data Barang setelah diubah:")
    tampilkan_barang()

# Hapus
def hapus_barang():
    if not gudang:
        print("Gudang kosong. Tidak ada barang yang tersedia.")
        return

    while True:
        kode_barang = input("Masukkan kode barang yang akan dihapus: ")
        if kode_barang in gudang:
            break
        else:
            print("Kode barang tidak ditemukan. Masukkan kode yang benar.")

    print(f"Data Barang sebelum dihapus:")
    tampilkan_barang()

    del gudang[kode_barang]

    print(f"Barang dengan kode {kode_barang} berhasil dihapus!")
    print(f"Data Barang setelah dihapus:")
    tampilkan_barang()

# Menu utama
while True:
    print("\n===== Aplikasi Manajemen Gudang =====")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Ubah Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        print("\nMenu Tampilkan Barang:")
        print("1. Tampilkan Semua Barang di Gudang")
        print("2. Cari Barang berdasarkan Kode Barang")
        submenu_pilihan = input("Pilih submenu: ")
        if submenu_pilihan == '1':
            tampilkan_barang()
        elif submenu_pilihan == '2':
            kode_cari = input("Masukkan Kode Barang yang ingin dicari: ")
            tampilkan_barang_berdasarkan_kode(kode_cari)
        else:
            print("Pilihan submenu tidak valid.")
    elif pilihan == '3':
        ubah_barang()
    elif pilihan == '4':
        hapus_barang()
    elif pilihan == '5':
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
