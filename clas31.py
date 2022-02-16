import sys

sys.path.append(r"C:/Users/wante/AppData/Local/Programs/Python/Python39")
class Oyuncu():     #bu bir taban sınıftır çünkü diğer 3 sınıfın ortak özelliklerini taşıyor.   
    def __init__(self , isim , rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 0
    def hareket_et(self):
        print("Hareket ediliyor...")
    def puan_kazan(self):
        print("Puan kazanıldı .")
    def puan_kaybet(self):
        print("Puan kaybedildi .")  
    
class Asker(Oyuncu):
    memleket = "Balıkesir"
    def hareket_et(self):
        print("Yeni hareket_et() metodu")

                #İşte bu şekilde bir sınıfın parantezleri içinde başka bir sınıfın adını belirtirsek,
                    # o sınıf, parantez içinde belirttiğimiz sınıfın bir alt sınıfı olmuş olur
class İsci(Oyuncu):
    pass

class Yonetici(Oyuncu):
    pass
