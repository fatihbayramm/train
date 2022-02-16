harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {}
for i in harfler:
    sozluk[i] = harfler.index(i)
print(sozluk)   
print("-"*30)
for i in range(len(harfler)):
    sozluk[harfler[i]]
print(sozluk)   

print("-"*100)

sozluk = {i:harfler.index(i) for i in harfler}
print(sozluk)
print("-"*100)

isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
sozluk = {i : len(i) for i in isimler}#sözlük üreteci kullanarak üstteki yöntemlerden daha kolay oluyor.
print(sozluk)