import math

# class bentuk
class Bentuk:
    def luas(self):
        return 0


# class persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


# class lingkaran 
class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return math.pi * (self.r ** 2)


# demonstrasi polymorphism
bentuk_list = [
    Bentuk(),
    Persegi(5),
    Lingkaran(7)
]

for b in bentuk_list:
    print(f"Luas: {b.luas()}")
