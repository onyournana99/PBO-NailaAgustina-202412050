class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Pembuatan object dosen
dosen1 = Dosen("Rianandya chandra hardika", "6861772673130322")
dosen2 = Dosen("Rachmah agus putri", "123456789")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Pemikiran desain"))
print(dosen2.ajar_mata_kuliah("Pemrograman berorientasi objek"))
