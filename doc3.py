f = open("../python.txt")
print(f.read())
print(f.read())
f.seek(0)#bu metot sayesinde dosya tekrar okunabiliyor .(0). bayt
print(f.read())
f.seek(10)#10.bayt dan başlıyor.
print(f.read())
print(f.tell())#dosyanın hangi bayt konumunda bulunduğunuzu öğrenmek isterseniz de tell() adlı
               # başka bir metottan yararlanabilirsiniz. Bu metodu parametresiz olarak kullanıyoruz.