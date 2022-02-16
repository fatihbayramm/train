import random

liste = ["ahmet", "mehmet", "sevgi", "sevim", "selin", "zeynep", "selim"]
a = random.sample(liste, 2)
print(a)
#random modülü içinde bulunan sample() adlı fonksiyon 
#herhangi bir dizi içinden istediğimiz sayıda rastgele numune almamızı sağlar

#random modülü içinde bulunan bir başka fonksiyon ise randrange() fonksiyonudur.
#Bu fonksiyon, belli bir aralıkta rastgele sayılar üretmemizi sağlar:
b = random.randrange(0 , 500)
print(b)