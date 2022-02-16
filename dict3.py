telefon_defteri = {"Ahmet Öz" : "0532 532 32 32",
                   "Mehmet Su": "0543 543 42 42",
                   "Seda Naz" : "0533 533 33 33",
                   "Eda Ala"  : "0212 212 12 12"}

kisi = input("Lütfen telefon numarasını öğrenmek istediğiniz kişinin adını girin :(Çıkmak için 'q') :")


if kisi in telefon_defteri:
    cevap = "{} adlı kişinin telefon numarası : {} "
    print(cevap.format(kisi , telefon_defteri[kisi]))
else:
    print("Lütfen geçerli bir isim giriniz .")    