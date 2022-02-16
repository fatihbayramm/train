class Giris():
    def __init__(self , mesaj = "Müşteri Numaranız : "):
        cevap = input(mesaj)
        print("Hoşgeldiniz ! ")
    @classmethod
    def paroladan(cls):
        mesaj = "Lütfen parolanızı giriniz : "
        cls(mesaj)    
    @classmethod
    def tcknden(cls):
        mesaj = "Lütfen TC Kimlik numaranızı giriniz : "
        cls(mesaj)    

Giris.paroladan()