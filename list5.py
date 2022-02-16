liste = []
while True:
    sayi = input("Bir sayı girin (Çıkmak için 'q') :")
    if sayi == "q":
        break
    sayi = int(sayi)
    if sayi not in liste:
        liste += [sayi]
        print(liste)
    else:
        print("Bu sayıyı daha önce girdiniz !")        