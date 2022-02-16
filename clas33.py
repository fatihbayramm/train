class Oyuncu():
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    def __init__(self , isim , rutbe):
        super().__init__(isim , rutbe)
        self.guc = 100
    def hareket_et(self):
        super().hareket_et()
        print("Hedefe ulaşıldı . ")      

class Yonetici(Oyuncu):
    def __init__(self , isim , rutbe):
        super().__init__(isim , rutbe)
        self.guc = 20
      

class İsci(Oyuncu):
    def __init__(self , isim , rutbe):
        super().__init__(isim , rutbe)
        self.guc = 70

asker = Asker("Fatih" , "Cpt")
print(asker.isim , asker.rutbe , sep=" --> ")  
isci = İsci("İsmail" , "Usta")
print(isci.isim , isci.rutbe , sep=" --> ")
print(asker.hareket_et())

              