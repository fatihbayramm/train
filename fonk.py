a = abs(-2)#bu fonk mutlak değerini verir.
print(a)
b = abs(2)
print(b)


c = divmod(10 , 2)#Bu fonksiyon, bir sayının bir sayıya bölünmesi işleminde bölümü ve kalanı verir.
print(c)

d = [12,14,15,16,17]
print(max(d))#en büyük değeri bulur max()

isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
           "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
print(max(isimler , key=len))# en uzun ismi de bulduk . 

print(min(d))
print(min(isimler , key=len))#bu fonk da en küçüğü bulur .

e = [10, 20, 43, 45 , 77, 2, 0, 1]
print(sum(e))#sayıları toplar.
print(sum(e , 10))#toplam değerin üstüne 10 sayısını ekler .

