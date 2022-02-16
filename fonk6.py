def carp(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    print(sonuc)
carp(1,2,3,4,5)  
carp(100)      

def func(**parametreler):
    print(parametreler)
func(isim = "Fatih" , soyisim = "Bayram" , sehir = "Balıkesir" , meslek = "Öğrenci")

def fonk(**bilgiler):
    print("-"*30)
    for anahtar , deger in bilgiler.items():
        print("{:<10} : {}".format(anahtar , deger))
    print("-"*30)
fonk(isim = "Fatih" , soyisim = "Bayram" , tel = "05511412851" , sehir = "Balıkesir")        
   