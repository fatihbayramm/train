print(help(dir)) 
#bilgi edinmek istediğimiz öğeyi help() fonksiyonuna parametre olarak vererek ilgili yardım dosyasına erişebiliyoruz.
print(help())

print("-"*60)

l = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31,
 120, 120, 236, 241, 123, 249, 364, 292, 153]
a = [i for i in l if i % 2 == 1 ]
print(a)

def tek(sayi):
    return sayi % 2 == 1

print(*filter(tek , l))#ilk parametre neye göre uygulanacağını , ikinci ise neyin üzerine uyg.
print(tek(12))
print(tek(3))
print(list(filter(tek , l)))

b = {i for i in filter(tek , l)}
print(b)
