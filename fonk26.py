l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dl = slice(0 , 3 , 2)
a = l[dl]
print(a)
#slice(başlangıç, bitiş, atlama)

b = [1, 2, 3]
print(sum(b))
c = [2,4,6]
print(sum(c , 10))#ikinci parametre toplam değerin üzerine ekler.

a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
d = zip(a1 , a2)#eşleştirme yapıyor. birinciyle birinci , ikinciyle ikinci...
d = list(d)
print(d)

for a , b in d:
    print(a,b)

    
isimler = ['ahmet', 'mehmet', 'zeynep', 'ilker']
yaslar = [25, 40, 35, 20]
eslesme = zip(isimler , yaslar)
for isim , yas in eslesme:
    print("İsim : {} / Yaş : {}".format(isim , yas))   



