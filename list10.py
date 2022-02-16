list1 = ["elma" , "armut"]
list1.append("kiraz")
print(list1)

isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
for i in platformlar :
    isletim_sistemleri.append(i)
print(isletim_sistemleri)    

list2 = [1 , 2 , 3]
for i in [4 , 5 , 6] :
    list2.append(i)
print(list2)    

sonuc = 1
while True :
    sayi = input("Sayı : (hesaplamak için 'q')")
    if sayi == "q":
        break
    sonuc *= int(sayi)
print(sonuc)        
