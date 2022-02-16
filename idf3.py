def selamla(kim):
    print("Merhaba" , kim)

selamla("YArram")    

def azalt(s):
    if len(s) < 1:
        return "bitti"
    else:
        print(list(s))
        return azalt(s[1:])

print(azalt("istihza"))

import sys
a = sys.getrecursionlimit()#özyineleme sınırı
print(a)
print("-"*30)
def ters_cevir(s):
    if len(s) < 1:
        return s 
    else:
        ters_cevir(s[1:])
        print(s[0])
d = ters_cevir("istihza")            
print(d)