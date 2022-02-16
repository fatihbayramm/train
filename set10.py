a = set([2, 4, 6, 8])
b = set([1, 3, 5, 7])
c = a.union(b)#union() metodu iki kümenin birleşimini almamızı sağlar.
print(c)

d = a | b #bu sembolle de aynı işlevi gerçekleştirebiliriz .
print(d)

kume = set(["elma", "armut", "kebap"])
yeni = [1, 2, 3]
kume.update(yeni)#for döngüsü kullanmadan kumeye yeni elemanlar ekleyebildik.
print(kume)
print("-"*60)

g = set([1, 2, 5])
j = set([1, 4, 5])
k = g.symmetric_difference(j)#kümelerin sadece birinde bulunan öğeleri verir .
print(k)