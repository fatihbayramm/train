kullanici_adi = input("Lütfen kullanıcı adınızı giriniz : ")
parola        = input("Lütfen parolanızı giriniz  : ")
karakter_uzunlugu = len(kullanici_adi) + len(parola)
mesaj ="Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor ."
print(mesaj.format(karakter_uzunlugu))
if karakter_uzunlugu > 40:
    print("Kullanıcı adı ile parolanızın " , 
    "toplam uzunluğu 40 karakteri geçmemelidir . ")
else:
    print("Sisteme Hoşgeldiniz ! ")    
    
    