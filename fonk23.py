#hash() Bu fonksiyon, belirli türdeki nesnelere bir karma değeri vermemizi sağlar.
print(hash("istihza"))
print(hash("python"))

#isinstance() tip denetimi için kullanabileceğimiz bir fonksiyon
a = isinstance("istihza" , str)
print(a)
b = isinstance("istihza" , list)
print(b)

#map() sayıların karelerini hesaplar .

l = [1, 4, 5, 4, 2, 9, 10]

def karesi(n):
    return n ** 2

c = list(map(karesi , l))
print(c)

#max() en büyüğü verir.

liste = [1, 2, 3]
print(max(liste))
print(max(1, 2, 3))

isimler = ['ahmet', 'can', 'mehmet', 'selin', 'abdullah', 'kezban']
print(max(isimler , key=len))

print("-"*40)

def en_yuksek_rutbe(rutbe):

    rutbeler = {'er'        : 0,
                'onbaşı'    : 1,
                'çavuş'     : 2,
                'asteğmen'  : 3,
                'teğmen'    : 4,
                'üsteğmen'  : 5,
                'yüzbaşı'   : 6,
                'binbaşı'   : 7,
                'yarbay'    : 8,
                'albay'     : 9}
    return rutbeler[rutbe]          

askerler = {'ahmet'     : 'onbaşı',
            'mehmet'    : 'teğmen',
            'ali'       : 'yüzbaşı',
            'cevat'     : 'albay',
            'berkay'    : 'üsteğmen',
            'mahmut'    : 'binbaşı'}

print(max(askerler.values() , key = en_yuksek_rutbe))

for k , v in askerler.items():
    if askerler[k] in max(askerler.values() , key = en_yuksek_rutbe):
        print(v , k)