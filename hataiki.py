while True:
    try:
        bolunen = input("Bir sayı girin (Çıkmak için : quit):")
        if bolunen == "23":
            raise Exception("Bu programda 23 sayısını görmek istemiyorum !")
        if bolunen == "quit":
            break
        bolen = input("Bir sayı daha : ")
        sayi1 = int(bolunen)
        sayi2 = int(bolen)
        print(sayi1/sayi2)
    except ValueError:
        print("Lütfen sayı girin ! ")
    except ZeroDivisionError:
        print("Bir sayı 0'a bölünemez ! ")
