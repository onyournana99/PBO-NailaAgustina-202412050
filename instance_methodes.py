class ManajerInventori:
    def __init__(self, nama_manajer):
        self.nama_manajer = nama_manajer
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah <= 0:
            return "Jumlah harus positif."

        self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
        return f"Stok {nama_barang} sekarang: {self.inventori[nama_barang]}"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang not in self.inventori:
            return f"Barang '{nama_barang}' tidak ditemukan."
        if jumlah <= 0:
            return "Jumlah harus positif."
        if self.inventori[nama_barang] < jumlah:
            return f"Stok tidak cukup. Stok saat ini: {self.inventori[nama_barang]}"

        self.inventori[nama_barang] -= jumlah

        if self.inventori[nama_barang] == 0:
            del self.inventori[nama_barang]
            return f"{nama_barang} habis dan dihapus dari inventori."
        
        return f"Stok {nama_barang} sekarang: {self.inventori[nama_barang]}"

    def lihat_inventori(self):
        if not self.inventori:
            return f"Inventori {self.nama_manajer} kosong."
        
        daftar = "\n".join([f"- {b}: {s} unit" for b, s in self.inventori.items()])
        return f"Inventori {self.nama_manajer}:\n{daftar}"



#  Demonstrasi
manajer = ManajerInventori("Budi")
print(manajer.lihat_inventori())
print(manajer.tambah_barang("Laptop", 10))
print(manajer.tambah_barang("Mouse", 50))
print(manajer.hapus_barang("Mouse", 20))
print(manajer.hapus_barang("Laptop", 15))
print(manajer.lihat_inventori())
