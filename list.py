liste = ["oge1" , "oge2", "oge3"]
print(type(liste))
liste2 = ["bir" , "iki" , 2 , 3 , ["uc" , "dort"] , 3.2]
print(type(liste2))
for oge in liste2:
    print("{} adlı ögenin veri tipi : {}".format(oge , type(oge)))

liste3 = [] #Boş bir liste
komut = dir(str)
print(type(komut))

a = "İstanbul Büyükşehir Belediyesi"
print(a[0])

b = a.split()
print(b[0])

diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
print(len(diller))

sayilar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayilar:
    print(range(*i))

