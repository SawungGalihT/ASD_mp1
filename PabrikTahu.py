class KasTahu:
    def __init__(self,bulan,tahun,saldo_tetap,pemasukan,pengeluaran):
        self.bulan = bulan
        self.tahun = tahun
        self.saldo = saldo_tetap
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran

class BukuKas:
    def __init__(self):
        self.data_kas = {}

    def tambah_data_kas(self,bulan,tahun,saldo_tetap,pemasukan,pengeluaran):
        data_baru = KasTahu(bulan,tahun,saldo_tetap,pemasukan,pengeluaran)
        self.data_kas[(bulan,tahun)] = data_baru

    def dapatkan_data_kas(self,bulan,tahun):
        return self.data_kas.get((bulan, tahun), None)
    
    def update_data_kas(self, bulan, tahun, pemasukan=None, pengeluaran=None, saldo=None):
        data_kas = self.dapatkan_data_kas(bulan, tahun)
        if data_kas:
            if pemasukan is not None:
                data_kas.pemasukan = pemasukan
            if pengeluaran is not None:
                data_kas.pengeluaran = pengeluaran
            if saldo is not None:
                data_kas.saldo = saldo - pengeluaran + pemasukan
            return True
        else:
            return False
        
    def hapus_data_kas(self,bulan,tahun):
        data_kas = self.dapatkan_data_kas(bulan,tahun)
        if data_kas:
            del self.data_kas[(bulan, tahun)]
            return True
        else:
            return False
        
bukukas = BukuKas()

bukukas.tambah_data_kas("Desember",2023,1000000,2000000,1600000)
bukukas.tambah_data_kas("ada",2023,1000000,2000000,1600000)


while True:
    print("Selamat Datang")
    print("Menu")
    print("1. Lihat Buku Kas")
    print("2. Tambahkan Data Baru")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilih = str(input("Masukkan Pilihan : "))

    if pilih == "1":
        print("")       
        print("Data Kas Bulanan:")
        for key, value in bukukas.data_kas.items():
            print(f"Bulan: {key[0]}, Tahun: {key[1]}")
            print("Saldo:", value.saldo)
            print("Pemasukan:", value.pemasukan)
            print("Pengeluaran:", value.pengeluaran)
            print("")

    elif pilih == "2":
        bulan = str(input("Masukkan Bulan Transaksi : "))
        tahun = int(input("Masukkan Tahun Transaksi : "))
        pemasukan = int(input("Masukkan Pemasukan Transaksi : "))
        pengeluaran = int(input("Masukkan Pengeluaran Transaksi : "))
        if len(bukukas.data_kas) > 0:
            bulan_terakhir, tahun_terakhir = list(bukukas.data_kas.keys())[-1]
            saldo_terakhir = bukukas.data_kas[(bulan_terakhir, tahun_terakhir)].saldo
            saldo_baru = saldo_terakhir + pemasukan - pengeluaran
            bukukas.tambah_data_kas(bulan, tahun, saldo_baru,pemasukan, pengeluaran)
            print("Data Berhasil Ditambahkan.")
            print("")
        else:
            saldo_terakhir = 0

    elif pilih == "3":
        bulan_hapus = str(input("Masukkan Nama Bulan dari Data yang ingin Dihapus : "))
        tahun_hapus = int(input("Masukkan Tahun dari Data yang ingin dihapus : "))
        hapus = bukukas.dapatkan_data_kas(bulan_hapus, tahun_hapus)
        if hapus:
            if bukukas.hapus_data_kas(bulan_hapus, tahun_hapus):
                print("Data kas berhasil dihapus.")
                print("")
            else:
                print("Gagal menghapus data.")
                print("")
        else:
            print("Data tidak ditemukan.")
            print("")

    elif pilih == "4":
        bulan_update = str(input("Masukkan Nama Bulan yang ingin Diperbarui : "))
        tahun_update = int(input("Masukkan Tahun yang ingin diperbarui : "))
        update = bukukas.dapatkan_data_kas(bulan_update, tahun_update)
        if update:
            pemasukan_baru = int(input("Masukkan Jumlah Pemasukan Baru : "))
            pengeluaran_baru = int(input("Masukkan Jumlah Pengeluaran Baru : "))
            saldo_baru = int(input("Masukkan Saldo Baru : "))
            
            if bukukas.update_data_kas(bulan_update, tahun_update, pemasukan_baru, pengeluaran_baru, saldo_baru):
                print("Data kas berhasil diperbarui.")
            else:
                print("Gagal memperbarui data.")
        else:
            print("Data tidak ditemukan.")
    
    elif pilih == "5":
        break
