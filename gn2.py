def uretec():
    yield "Merhaba"
    yield "Dünya"

g = uretec()
print(next(g))
print(next(g))   

def uretec2():
    print("üreteç ilk defa next fonksiyonu ile kullanıldı.")
    yield "1. yield"
    print("üreteç ikinci defa next fonksiyonu ile kullanıldı.")
    yield "2. yield"
    print("üreteç üçüncü defa next fonksiyonu ile kullanıldı ve bitti.")

g = uretec2()
print(next(g))
print(next(g))
