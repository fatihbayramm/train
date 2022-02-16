def ters_cevir(s):
    if len(s) < 1:
        return s 
    else:
        return ters_cevir(s[1:]) + s[0]

kelime = input("Lütfen kelimenizi giriniz : ")
print("Girdiğiniz kelimenin tersi : {}".format(ters_cevir(kelime)))       

def ters(s):
    if not s:
        return s 
    else:
        return s[-1] + ters(s[:-1])

print(ters("istihza"))            