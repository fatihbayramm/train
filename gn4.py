def yaz(sayi):
    for i in range(sayi):
        print("Merhaba Dünya !")
        yield

y = yaz(4)
for i in y:
    print(i)

print("-"*30)    


def uretec1():
    yield "Üreteç 1 başladı."
    yield "Üreteç 1 bitti ."

def uretec2():
    yield "Üreteç 2 başladı ."
    yield from uretec1()#burada üreteç 1 i kullandık yield from deyimi sayesinde.
    yield "Üreteç 2 bitti ."

for i in uretec2():
    print(i)