kontrol = []
sonuc = 1
while True:
    sayi = input("Sayı (Hesaplamak için 'q') : ")
    if sayi == "q" :
        break
    kontrol.append(sayi)
    sonuc *= int(sayi)
if len(kontrol) < 2:
    print("Yeterli sayı girilmedi ! ")
else:
    print(sonuc)        