import random

def sayi_uret(baslangıc = 0 , bitis = 500 , adet = 6):
    sayilar = set()

    while len(sayilar) < adet:
        sayilar.add(random.randrange(baslangıc , bitis))

    return sayilar

print(*sayi_uret(1 , 10 , 2) , sep="-")
