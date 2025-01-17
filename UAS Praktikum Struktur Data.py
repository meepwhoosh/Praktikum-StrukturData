import datetime

class Task:
    def __init__(self, nama, deskripsi, tenggat_waktu, status="Belum Selesai"):
        self.nama = nama
        self.deskripsi = deskripsi
        self.tenggat_waktu = tenggat_waktu
        self.status = status

def buat_tugas():
    nama = input("Masukkan nama tugas: ")
    deskripsi = input("Masukkan deskripsi tugas: ")

    while True:
        try:
            tanggal_str = input("Masukkan tenggat waktu (YYYY-MM-DD): ")
            tenggat_waktu = datetime.datetime.strptime(tanggal_str, "%Y-%m-%d")
            
            if tenggat_waktu < datetime.datetime.now():
                print("Tenggat waktu harus di masa depan. Silakan masukkan kembali.")
                continue
            break
        except ValueError:
            print("Format tanggal tidak valid. Silakan masukkan format YYYY-MM-DD.")

    return Task(nama, deskripsi, tenggat_waktu, status="Belum Selesai")

def tampilkan_tugas(tugas):
    print(f"Nama: {tugas.nama}")
    print(f"Deskripsi: {tugas.deskripsi}")
    print(f"Tenggat Waktu: {tugas.tenggat_waktu.strftime('%Y-%m-%d')}")
    print(f"Status: {tugas.status}")

def urutkan_tugas(tugas):
    def compare_by_tenggat_waktu_and_status(task):
        return (task.tenggat_waktu, task.status)

    return sorted(tugas, key=compare_by_tenggat_waktu_and_status)


def tambahkan_ke_daftar_tugas(tugas, daftar_tugas):
    daftar_tugas.append(tugas)

def hapus_dari_daftar_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
        return None
    return daftar_tugas.pop(0)

def tampilkan_daftar_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
        return
    for tugas in daftar_tugas:
        tampilkan_tugas(tugas)
        print("-------------------")

def ubah_status(tugas, status_baru):
    tugas.status = status_baru

def ubah_status_tugas(nama_tugas, daftar_tugas, status_baru):
    for tugas in daftar_tugas:
        if tugas.nama == nama_tugas:
            ubah_status(tugas, status_baru)
            print(f"Status tugas '{nama_tugas}' berhasil diubah menjadi '{status_baru}'.")
            return
    print(f"Tugas '{nama_tugas}' tidak ditemukan.")

def main():
    daftar_tugas = []

    while True:
    
        print("Pengelola Tugas Sederhana")
        print("-----------------------------")

        print("1. Tambahkan Tugas")
        print("2. Urutkan Tugas")
        print("3. Menghapus")
        print("4. Tampilkan Tugas")
        print("5. Ubah Status Tugas")
        print("6. Keluar")

        pilihan = input("Masukkan Pilihan Anda: ")

        if pilihan == "1":
            tugas_baru = buat_tugas()
            if tugas_baru:
                tambahkan_ke_daftar_tugas(tugas_baru, daftar_tugas)
                print("Tugas baru telah ditambahkan.")
        elif pilihan == "2":
            queue = urutkan_tugas(daftar_tugas)
            print("Tugas telah diurutkan berdasarkan tenggat waktu dan status.")
        elif pilihan == "3":
            tugas = hapus_dari_daftar_tugas(daftar_tugas)
            if tugas:
                tampilkan_tugas(tugas)
                print("Tugas telah dihapus.")
        elif pilihan == "4":
            tampilkan_daftar_tugas(daftar_tugas)
        elif pilihan == "5":
            if not daftar_tugas:
                print("Belum ada tugas yang dibuat.")
                continue
            nama_tugas = input("Masukkan nama tugas yang ingin diubah statusnya: ")
            status_baru = input("Masukkan status baru (Selesai/Belum Selesai): ")
            ubah_status_tugas(nama_tugas, daftar_tugas, status_baru)
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
