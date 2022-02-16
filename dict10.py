sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}

print(sozluk.items())       

for anahtar , deger in sozluk.items():
    print("{} = {}".format(anahtar , deger))


ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız :")
if sorgu not in ing_sözlük:
    print("Lütfen veri tabanında olan bir kelimeyi sorgulayınız !")
else:
    print(ing_sözlük[sorgu])        