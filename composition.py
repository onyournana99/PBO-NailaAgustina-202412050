# Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama


# Class Buku 
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis   

    def info(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"


# Instansiasi objek
p = Penulis("Naila Agustina")
b = Buku("Pemrograman berorientasi objek", p)

# Demonstrasi akses data penulis 
print(b.info())
print(b.penulis.nama)        