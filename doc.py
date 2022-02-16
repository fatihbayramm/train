ths = open("../tahsilat_dosyası.txt" , "w")
ths.write("""Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34""")
ths.close()

ths = open("../tahsilat_dosyası.txt" , "r")
print(ths.read())#dosyanın tamamını okuyor.
ths.close()
print("-"*30)
ths = open("../tahsilat_dosyası.txt" , "r")
print(ths.readline())#dosyayı satır satır sırayla okuyor .
print(ths.readline())
print(ths.readline())
ths.close()

ths = open("../tahsilat_dosyası.txt" , "r")
print(ths.readlines())#verileri liste biçiminde veriyor.
ths.close()
