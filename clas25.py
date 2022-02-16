class Falanca():
    _yarigizli = "yarıgizliüye"

class Calisan():
    _personel = []

    def __init__(self , isim):
        self._isim = isim
        self.personel_ekle()

    def personel_ekle(self):
        self._personel.append(self._isim)
        print("{} adlı kişi personel listesine eklendi ! ".format(self._isim))
    @classmethod
    def personeli_goruntule(cls):
        print("Personel Listesi : ")
        for kisi in cls._personel:
            print(kisi)     
    @property
    def isim(self):
        return self._isim
    @isim.setter            
    def isim_degistir(self , yeni_isim):
        kisi = self._personel.index(self.isim)
        self._personel[kisi] = yeni_isim
        print("yeni isim : " , yeni_isim )


c1 = Calisan("Fatih")
c2 = Calisan("Enes")
c3 = Calisan("Ahmet")

Calisan.personeli_goruntule()



print("-"*30)

Calisan.personeli_goruntule()

print("-"*30)

kisi = Calisan._personel.index("Fatih")
Calisan._personel[kisi] = "İsmail"

Calisan.personeli_goruntule()
print("-"*30)

c3.isim_degistir("Berke")

Calisan.personeli_goruntule()

c3.isim("Arda")
print("-"*30)
Calisan.personeli_goruntule()
