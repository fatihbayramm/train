kisiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}
isim = "Hakkında ayrıntılı bilgi \
edinmek istediğiniz kişinin adını girin : "

arama = input(isim)
ayrinti = input("Memleket / Meslek / Yaş ? --> ")

print(kisiler[arama][ayrinti])
