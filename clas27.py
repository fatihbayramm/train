class Yazilim():
    def __init__(self):
        self.veri = 0
    @property
    def data(self):
        return self.veri
p = Yazilim()
#p.data = 5 kodu hata  verir.

class Program():
    def __init__(self):
        self._sayi = 0
    @property
    def sayi(self):        
        return self._sayi
    @sayi.setter
    def sayi(self , yeni_deger):
        self._sayi = yeni_deger
        return self._sayi

a = Program()
print(a.sayi)       

a.sayi = 10

print(a.sayi)
