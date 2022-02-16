while True:
    ilk_sayi = input("Bir sayı girin (Çıkmak için q) : ")
    if ilk_sayi == "q":
        break

    ikinci_sayi = input("Bir sayı daha :")
    try:
        sayi1 = int(ilk_sayi)
        sayi2 = int(ikinci_sayi)
        print(sayi1 , "/" , sayi2 , "=" , sayi1 / sayi2)
    except ValueError as hata:
        print("Lütfen sadece sayı girin ! ")
        print("Orijinal hata mesajı :" , hata)
    except ZeroDivisionError:
        print("Bir sayı 0'a bölünemez !")            