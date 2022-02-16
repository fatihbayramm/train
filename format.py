kalkis       = input("Kalkış yeri: ")
varis        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayisi = input("Bilet sayısı: ")
metin ="{0} noktasından {1} noktasına, 14:30 hareket saatli \
sefer için {2} adına {3} adet bilet ayrılmıştır!"
print(metin.format(kalkis , varis , isim_soyisim , bilet_sayisi))

kodlama  = "utf-8"
site_adı = "Python Programlama Dili"
dosya    = open("deneme.html", "w", encoding=kodlama)
içerik   = """
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset={}" />
    <title>{}</title>
</head>

<body>
    <h1>istihza.com web sitesine hoş geldiniz!</h1>
    <p><b>{}</b> için bir Türkçe belgelendirme projesi...</p>
</body>

</html>
"""

print(içerik.format(kodlama, site_adı, site_adı), file=dosya)

dosya.close()

print("{dil} dersleri".format(dil = "python"))

for sira , karakter in enumerate(dir("")):
    if sira % 3 == 0:
        print("\n" , end ="")
    print("{:<20}".format(karakter) , end ="")    
