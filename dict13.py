hava_durumu = {"İstanbul": "yağmurlu", "Adana": "güneşli", "İzmir": "bulutlu"}
yedek_hava_durumu = hava_durumu
print(yedek_hava_durumu)

yedek_hava_durumu["Mersin"] = "sisli"
print(hava_durumu)#sözlüklerin birinde yapılan değişiklik diğerini de etkiledi.
print(yedek_hava_durumu)
print("-"*70)

hd = {"İstanbul": "yağmurlu", "Adana": "güneşli" , "İzmir": "bulutlu"}
yd = hd.copy()
hd["Mersin"] = "sisli"#Gördüğümüz gibi burada orijinalinde değişiklik yaptık ama yd de bir değişilik olmadı .
print(hd)             #copy() metodu sayesinde . 
print(yd)