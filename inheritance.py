# class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: {self.nama}, umur {self.umur} tahun"


# class Mahasiswa 
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)   # memanggil constructor parent class
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, umur {self.umur} tahun, NIM {self.nim}"


# instansiasi objek
p = Person("Naila", 20)
m = Mahasiswa("Naila", 20, "230511000")

# Panggil method info()
print(p.info())
print(m.info())
