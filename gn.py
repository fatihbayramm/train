def fonksiyon_sayici():
    sayi = 0
    def say():
        nonlocal sayi
        sayi += 1
        return sayi
    return say

def uretec_sayici():
    sayi = 0
    while True:
        sayi += 1
        yield sayi

fonk = fonksiyon_sayici()
uretec = uretec_sayici()
print(fonk())
print(fonk())
print(fonk())
print(fonk())

print("-"*30)

print(next(uretec))
print(next(uretec))
print(next(uretec))
print(next(uretec))

print(type(uretec))
print(type(fonk))