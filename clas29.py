import sys
sys.path.append(r"C:/Users/wante/AppData/Local/Programs/Python/Python39")

class Asker():
    def __init__(self , isim , rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 100
    def hareket_et(self):
        print("Hareket ediliyor...")
    def puan_kazan(self):
        print("Puan kazanıldı .")
    def puan_kaybet(self):
        print("Puan kaybedildi .")

class İsci():
    def __init__(self , isim , rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 70
    def hareket_et(self):
        print("Hareket ediliyor...")
    def puan_kazan(self):
        print("Puan kazanıldı .")
    def puan_kaybet(self):
        print("Puan kaybedildi .") 

class Yonetici():
    def __init__(self , isim , rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 20
    def hareket_et(self):
        print("Hareket ediliyor...")
    def puan_kazan(self):
        print("Puan kazanıldı .")
    def puan_kaybet(self):
        print("Puan kaybedildi .")    

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
