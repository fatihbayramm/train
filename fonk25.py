a = pow(2 , 3 , 2)
print(a)
print("-"*20)
#pow() kuvvet alır. 2'nin üçüncu kuvveti. Son parametre ise modülüsdür.
range(0 , 10 , 2)#son parametre atlama değeridir.
for i in range(0 , 10 , 2):
    print(i)
b = [i for i in range(0 , 10 , 2)]
print(b)    

isimler = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']

c = list(reversed(isimler))
print(c)
print("-"*30)

print(sorted("ahmet"))#alfabetik sıralar.
print(sorted(('elma', 'armut', 'kiraz', 'badem')))
print(sorted(['elma', 'armut', 'kiraz', 'badem']))

print("-"*30)

isimler2 = ['ahmet', 'çiğdem', 'ışık', 'şebnem', 'zeynep', 'selin']
print(sorted(isimler2))#türkçe karakterleri düzgün sıralayamıyor.
import locale
locale.setlocale(locale.LC_ALL , "Turkish_Turkey.1254")
print(sorted(isimler2 , key =locale.strxfrm))#locale adlı modülü içe aktardıktan sonra bunları yazdık ve oldu.

print(sorted('afgdhkıi', key=locale.strxfrm))#bu da sorunlu çıktı...

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

cevrim = {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4,
          'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9,
          'ı': 10, 'i': 11, 'j': 12, 'k': 13,
          'l': 14, 'm': 15, 'n': 16, 'o': 17,
          'ö': 18, 'p': 19, 'r': 20, 's': 21,
          'ş': 22, 't': 23, 'u': 24, 'ü': 25,
          'v': 26, 'y': 27, 'z': 28}

cevrim2 = {i: harfler.index(i) for i in harfler}
print(cevrim2)

def sırala(kelime):
    return ([cevrim.get(kelime[i]) for i in range(len(kelime))])

isimler3 = ["ahmet", "ışık", "ismail",
           "çiğdem", "can", "şule" , "iskender"]

print(*sorted(isimler3 , key = sırala) , sep = "\n")


