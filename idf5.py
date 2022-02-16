def sayac(sayi , sinir):
    print(sayi)
    if sayi == sinir :
        return "bitti!"
    else:
        return sayac(sayi-1 , sinir)   
print(sayac(100 , 0))       

l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

def duz_liste_yap(liste):
    if not isinstance(liste , list):
        return [liste]
    elif not liste:
        return []
    else:
        return duz_liste_yap(liste[0]) + duz_liste_yap(liste[1:])

print(duz_liste_yap(l))

