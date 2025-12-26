class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} berwarna {self.warna}, tahun {self.tahun}"


# Instansiasi object kendaraan
mobil1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
motor1 = Kendaraan("Honda Beat", "Merah", 2022)

# Output instansiasi
print(mobil1.info_kendaraan())
print(motor1.info_kendaraan())

# Akses class attribute
print(f"Bahan bakar mobil: {mobil1.bahan_bakar}")
print(f"Bahan bakar motor: {motor1.bahan_bakar}")

# Akses langsung melalui nama class
print(f"Jenis bahan bakar (class): {Kendaraan.bahan_bakar}")
