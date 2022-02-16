print("-"*100)
dilekce = """

                                                            Tarih : {}

T.C.
{} Üniversitesi
{} Fakültesi Dekanlığına
Fakülteniz {} Bölümü {} numaralı öğrencisiyim . Ekte sunduğum belgede 
belirtilen mazeretim gereğince {} Eğitim-Öğretim yılı {} . yarıyılında
öğrenime ara izni (kayıt dondurma) istiyorum .

    Bilgilerinizi ve gereğini arz ederim .

        İmza
   Ad              : {}
   Soyad           : {}
   T.C. Kimlik No. : {}
   Adres           : {}
   Tel.            : {}   
   Ekler           : {}   
   """             
tarih         = input("Tarih :")
universite    = input("Üniversite adı :")
fakulte       = input("Fakülte adı : ") 
bolum         = input("Bölüm adı : ")
ogrenci_no    = input("Öğrenci numarası :")
ogretim_yili  = input("Öğretim Yılı :")
yariyil       = input("Yarıyıl :")
ad            = input ("Öğrencinin adı :")
soyad         = input("Öğrencinin soyadı : ")
tc_kimlik_no  = input("TC Kimlik no. :")
adres         = input("Adres :")
tel           = input("Telefon numarası :")
ekler         = input("Ekler :")

print(dilekce.format(tarih , universite , fakulte , bolum , ogrenci_no , ogretim_yili , 
yariyil , ad , soyad , tc_kimlik_no , adres , tel , ekler ) )
print("-"*100)

