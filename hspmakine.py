giris = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """
print(giris)
a = 1
while a == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını girin  (Çıkmak için 'q') : ")
    if soru == "q":
        print("Çıkılıyor...")
        a = 0
    elif soru == "1":
        sayi1 = int(input("İlk sayı :"))
        sayi2 = int(input("İkinci sayı :"))
        print("%s + %s = %s"%(sayi1 , sayi2 , sayi1 + sayi2))
    elif soru == "2":
        sayi3 = int(input("İlk sayı :"))
        sayi4 = int(input("İkinci sayı :"))
        print("%s - %s = %s"%(sayi3 , sayi4 , sayi3 - sayi4))    
    elif soru == "3":
        sayi5 = int(input("İlk sayı :"))
        sayi6 = int(input("İkinci sayı : "))
        print("%s x %s = %s"%(sayi5 , sayi6 , sayi5 * sayi6))
    elif soru == "4":
        sayi7 = int(input("İlk sayı :"))
        sayi8 = int(input("İkinci sayı :"))
        print("%s / %s = %s"%(sayi7 , sayi8 , sayi7 / sayi8))
    elif soru == "5":
        sayi9 = int(input("İlk sayı :"))
        print("%s ^ 2 =%s"%(sayi9 , sayi9 ** 2))
    elif soru == "6":
        sayi10 = int(input("İlk sayı :"))
        print("Karekök %s = %s"%(sayi10 , sayi10 ** 0.5))    
    else:
        print("Yanlış giriş !")
        print("Lütfen aşağıdaki değerlerden birini giriniz ." , giris)
            

            
