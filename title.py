degisken = "istanbul büyüksehir belediyesi "
if degisken.startswith("i"):
    degisken = "İ" + degisken[1:]
degisken = degisken.title()
print(degisken)    
