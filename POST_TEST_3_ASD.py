# NAMA: MUTHMAINNAH AISYAH
# NIM: 2209116001
# KELAS: SI - A 2022

# LINKED LIST - POST TEST 3

import os
from prettytable import PrettyTable
os.system("cls")

# Membuat class untuk node
class Node_jilbab:
    def __init__(self, tanggal, nama, jilbab, warna, harga, prev_node=None, next_node=None):
        self.tanggal = tanggal
        self.nama = nama
        self.jilbab = jilbab
        self.warna = warna
        self.harga = harga
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return str(self.tanggal, self.nama, self.jilbab, self.warna, self.harga)

# Membuat class untuk linked list
class Linked_jilbab:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history_1 = []
        self.history_2 = []
    
    def display_data(self):
        n = self.head
        table_data = PrettyTable(["No", "Tanggal", "Nama Pelanggan", "Model Jilbab", "Warna Jilbab", "Harga Jilbab"])
        no = 1
        if n is None:
            print("Data Tidak Ada!")
        else:
            while n is not None:
                table_data.title = "DATA PELANGGAN"
                table_data.add_row([no, n.tanggal, n.nama, n.jilbab, n.warna, n.harga])
                no += 1
                n = n.next
            print(table_data)

    def insert_data(self, tanggal, nama, jilbab, warna, harga):
        if self.head is None:
            self.head = Node_jilbab(tanggal, nama, jilbab, warna, harga)
            self.tail = self.head
        else:
            self.tail.next = Node_jilbab(tanggal, nama, jilbab, warna, harga)
            self.tail = self.tail.next
        self.history_1.append((tanggal, nama, jilbab, warna, harga)) 
        return self.tail

    def delete_data(self, letak):
        n = self.head
        if self.head is None:
            os.system("cls")
            print("Data Tidak Ada!")
        elif letak == 1:
            self.head = n.next
            os.system("cls")
            print("Data Berhasil Dihapus!")
        else:
            count = 1
            while n is not None and count != letak:
                prev = n
                n = n.next
                count += 1
            if n is None:
                os.system("cls")
                print("Data Tidak Ditemukan!")
            else:
                prev.next = n.next
                os.system("cls")
                print("Berhasil Dihapus!")
                self.display_data()
        self.history_2.append((n.tanggal, n.nama, n.jilbab, n.warna, n.harga))   

    def history_masuk(self):
        table_history = PrettyTable(["No", "Tanggal", "Nama Pelanggan", "Model Jilbab", "Warna Jilbab", "Harga Jilbab"])
        no = 1
        table_history.title = "HISTORY TAMBAH DATA"
        for i in self.history_1:
            table_history.add_row([no, i[0], i[1], i[2], i[3], i[4]])
            no += 1
        print(table_history)

    def history_keluar(self):
        table_history = PrettyTable(["No", "Tanggal", "Nama Pelanggan", "Model Jilbab", "Warna Jilbab", "Harga Jilbab"])
        no = 1
        table_history.title = "HISTORY HAPUS DATA"
        for i in self.history_2:
            table_history.add_row([no, i[0], i[1], i[2], i[3], i[4]])
            no += 1
        print(table_history)

    def pagination(self, halaman, jumlah):
        n = self.head
        table_halaman = PrettyTable(["No", "Tanggal", "Nama Pelanggan", "Model Jilbab", "Warna Jilbab", "Harga Jilbab"])
        no = (halaman - 1) * jumlah + 1
        table_halaman.title = "Halaman {}".format(halaman)
        count = 0
        while n != None:
            if count >= (halaman - 1) * jumlah and count < halaman * jumlah:
                table_halaman.add_row([no, n.tanggal, n.nama, n.jilbab, n.warna, n.harga])
                no += 1
            count += 1
            n = n.next
        print(table_halaman)

# Membuat fungsi menu
def menu():
    print("="*40)
    print("MENU PENDATAAN PELANGGAN DI TOKO JILBAB")
    print("="*40)
    print("1. Lihat Data Pelanggan\n2. Tambah Data Pelanggan\n3. Hapus Data Pelanggan\n4. History Tambah Data")
    print("5. History Hapus Data\n6. Halaman Data Pelanggan\n7. Exit")
    print("="*40)   

# Shortcut Class
jilbab = Linked_jilbab()

# Masukkan Data
jilbab.insert_data("15/03/2023", "Muthmainnah", "Pashmina", "Coklat", 65000)
jilbab.insert_data("15/03/2023", "Aisyah", "Bergo", "Hitam", 35000)
jilbab.insert_data("15/03/2023", "Armeynita", "Paris", "Maroon", 50000)
jilbab.insert_data("16/03/2023", "Diah", "Pashmina", "Navy", 65000)
jilbab.insert_data("16/03/2023", "Indah", "Plisket", "Hitam", 55000)
jilbab.insert_data("16/03/2023", "Adelia", "Sport", "Abu", 30000)
jilbab.insert_data("16/03/2023", "Mumtaz", "Paris", "Sage", 50000)

# Program berjalan
while True:
    try:
        menu()
        tanya = input("Masukkan Pilihan: ")
        if tanya == "1":
            os.system("cls")
            jilbab.display_data()
        elif tanya == "2":
            os.system("cls")
            tanggal_baru = input("Masukkan Tanggal: ")
            nama_pelanggan = input("Masukkan Nama: ")
            nama_jilbab = input("Masukkan Model Jilbab: ")
            warna_jilbab = input("Masukkan Warna Jilbab: ")
            harga_jilbab = int(input("Masukkan Harga Jilbab: "))
            jilbab.insert_data(tanggal_baru, nama_pelanggan, nama_jilbab, warna_jilbab, harga_jilbab)
            os.system("cls")
            print("Berhasil Ditambahkan!")
            jilbab.display_data()
        elif tanya == "3":
            os.system("cls")
            jilbab.display_data()
            no = int(input("Masukkan Angka Yang Ingin Dihapus: "))
            jilbab.delete_data(no)
        elif tanya == "4":
            os.system("cls")
            jilbab.history_masuk()
        elif tanya == "5":
            os.system("cls")
            jilbab.history_keluar()
        elif tanya == "6":
            os.system("cls")
            jilbab.pagination(1, 5)
            lanjut = str(input("Lanjut Mencari (y/t): "))
            while lanjut == "y":
                halaman = int(input("Masukkan Halaman: "))
                os.system("cls")
                jilbab.pagination(halaman, 5)
                lanjut = str(input("Lanjut Mencari (y/t): "))
            else:
                os.system("cls")
                continue
        elif tanya == "7":
            os.system("cls")
            print("="*40)
            print("Program Telah Berhenti!")
            print("="*40)
            exit()
        else:
            os.system("cls")
            print("Masukkan Dengan Benar!")
    except ValueError:
        os.system("cls")
        print("Format Salah!")
