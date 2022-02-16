sozluk = {"sıfır": 0,
          "bir"  : 1,
          "iki"  : 2,
          "üç"   : 3,
          "dört" : 4,
          "beş"  : 5}

print(sozluk["bir"])
sozluk2 = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
          "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
          "Seda Bayrak"    : ["İskenderun", "Doktor", 30]}

print(sozluk2["Seda Bayrak"])   

kisiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}

print(kisiler["Ahmet Özkoparan"]["Memleket"])     
print(kisiler["Mehmet Yağız"]["Meslek"])   
print(kisiler["Seda Bayrak"]["Yaş"])                       