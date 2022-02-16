import sys
sys.path.append(r"C:/Users/wante/AppData/Local/Programs/Python/Python39")



class Calisan():
    __personel = []

    def __init__(self , isim):
        self.isim = isim
        self.kabiliyet = []
        self.__personele_ekle()  
    @classmethod    
    def personel_sayisi_goruntule(cls):
        print(len(cls.__personel))    
    def __personele_ekle(self):
        self.__personel.append(self.isim)
        print("{} adlı kişi personele eklendi !" .format(self.isim))
    @classmethod    
    def personeli_goruntule(cls):
        print("Personel Listesi")
        for kisi in cls.__personel:
            print(kisi)
    def kabiliyet_ekle(self , kabiliyet):
        self.kabiliyet.append(kabiliyet)
    def kabiliyetleri_goruntule(self):
        print("{} adlı kişinin kabiliyetleri :".format(self.isim))
        for kabiliyet in self.kabiliyet:
            print(kabiliyet)    
