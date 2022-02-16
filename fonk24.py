#min() fonksiyonu da bir dizi içindeki en küçük öğeyi bulur. Bu fonksiyonun kullanımı max() ile aynıdır.
f = open("../ni.txt" , "w" , buffering = 1 , encoding = "utf-8" , errors = "replace" , newline = "\n")
f.write("birinci satır\n")
f.write("ikinci satır\n")
f.write("aaa")
f.write("\n")
#buffering parametresi bu 1 değerini yalnızca metin kipinde alabilir.
#buffering parametresi verileri tampondan aldıktan sonra satır satır işler değeri 1 olursa .
#bu parametre 0 olursa verileri tampona almadan doğrudan dosyaya işler .
#fileno() dosya tanımlayıcısı.
print(f.fileno())#Her dosyanın dosya tanımlayıcısı benzersizdir:
#Python’da bir dosyayı open() fonksiyonuyla açarken
#dosya adını vermenin yanı sıra, dosyanın tanımlayıcısını da kullanabilirsiniz:
z = open(3)
z = open(f.fileno())
