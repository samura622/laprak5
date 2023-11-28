# Fungsi untuk menyimpan data ke file
def simpan_ke_file(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line + '\n')

# Fungsi untuk membaca data dari file dan menghapus duplikat
def baca_dan_hapus_duplikat(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    unique_lines = list(set(lines))
    return unique_lines

# Data yang diberikan
data = [
    "Andi,11119,1",
    "Bima,11112,1",
    "Rahma,11131,3",
    "Zeno,11198,9",
    "Rahma,11131,3",
    "Andi,11119,1"
]

file_path = "data_mahasiswa.txt"

# Simpan data awal ke file
simpan_ke_file(file_path, data)

while True:
    print("===== MENU =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Duplikat")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        semester = input("Masukkan Semester: ")
        data_baru = f"{nama},{nim},{semester}"
        data.append(data_baru)
        simpan_ke_file(file_path, data)
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        data_dari_file = baca_dan_hapus_duplikat(file_path)
        for line in data_dari_file:
            print(line.strip())

    elif pilihan == "3":
        data_bersih = baca_dan_hapus_duplikat(file_path)
        simpan_ke_file(file_path, data_bersih)
        print("Duplikat berhasil dihapus.")

    elif pilihan == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-4.")
