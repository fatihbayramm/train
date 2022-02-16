elemanlar = ("Ahmet" , "Mehmet" , "Fatih")
adres = dict.fromkeys(elemanlar , "Kadıköy")
print(adres)

sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"),
"içecekler": ("su", "kola", "ayran")}
print(sepet.pop("meyveler"))
print(sepet)
print(sepet.pop("tatlılar" , "Silinecek öğe yok !"))

print("-"*60)

fruits = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
fruits.setdefault("içecekler" , ("su" , "kola"))
print(fruits)
print(fruits.setdefault("meyveler" , ("kiraz" , "şeftali")))
#setdefault() metoduyla ekleme yapabiliriz ama eklemeye çalıştıgımız anahtar zaten varsa
#onun değerlerini eklemez , var olan anahtarın değerlerini ekrana verir  . 
