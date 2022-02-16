def kare_bul(sayi):
    cikti = "{} sayısının karesi {} , karekökü ise {} sayısıdır ."
    print(cikti.format(sayi , sayi**2 , sayi**0.5))
kare_bul(2)  
kare_bul(15)  
kare_bul(16)

def uzunluk(kelime):
    c = 0
    for i in kelime :
        c += 1
    print(c)
uzunluk("fatih")        
uzunluk("ismail")
liste = ["ahmet", "mehmet", "veli"]
uzunluk(liste)
tuples = (1 , 2 , 3 , 4)
uzunluk(tuples)
kume = set([1 , 2 , 3 , 4 , 5])
uzunluk(kume)