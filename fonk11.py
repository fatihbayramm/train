x = []
print("x\ 'in ilk hali : ",x)

def degistir():
    print("x\ 'i değiştiriyoruz...")
    x.append(1)
    return x
degistir()
print("x\ 'in son hali :",x)    
print("-"*70)

isim = "Fırat"
def fonk():
    global isim
    isim += " Özgül"
    return isim
print(fonk())    