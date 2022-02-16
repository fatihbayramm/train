ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız :")
print(ing_sözlük.get(sorgu , "Bu kelime veritabanımızda yoktur !"))
#get() metodunda ilk parametre kelime sözlükte varsa onun değerini verir
#eğer kelime sözlükte yoksa ikinci parametre çalışır .

soru = input("Hava durumunu öğrenmek istediğiniz şehrin adını girin :")
if soru == "istanbul":
    print("Açık ve güneşli")
elif soru == "ankara":
    print("yağışlı")
elif soru == "balıkesir":
    print("bulutlu")        
else:
    print("Bu şehre ait hava durumu bilgisi bulunmamaktadır !")    

print("-"*60)

question = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")
cevap = {"istanbul": "gök gürültülü ve sağanak yağışlı",
         "ankara": "açık ve güneşli", "izmir": "bulutlu"}
print(cevap.get(question , "Bu şehir veritabanımızda yoktur !"))         

