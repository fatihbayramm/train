def kopyala(kaynak_dosya , hedef_dizin):
    cikti = "{} adlı dosya {} adlı dizin içine kopyalandı !"
    print(cikti.format(kaynak_dosya , hedef_dizin))
kopyala("final_takvimi" , "Users\wante\Desktop" )    

def kayit_olustur(isim , soyisim , issis , sehir):
    print("-"*30)
    print("İsim            :" , isim)
    print("Soyisim         :" , soyisim)
    print("İşletim Sistemi :" , issis)
    print("Şehir           :" , sehir)
    print("-"*30)
kayit_olustur("Fatih" , "Bayram" , "Win10" , "İstanbul")    
kayit_olustur(sehir = "Balıkesir" , issis = "WinXp" , soyisim ="Bayram" , isim = "Mehmet")