def fonk(param1 , param2):
    return param1 + param2

a = fonk(2,3)
print(a)

topla = lambda param1 , param2 : param1 + param2
b = topla(3 , 4)
print(b)

def cift_mi(sayi):
    return sayi % 2 == 0
print(cift_mi(2))    

cift = lambda sayi : sayi % 2 == 0
c = cift(4)
print(c)
d = cift(3)
print(d)

l = [2, 5, 10, 23, 3, 6]
for i in l:
    print(i**2)

f = [i**2 for i in l]
print(f)

print(*map(lambda sayi : sayi**2 , l))

def karesi(sayi):
    return sayi**2

print(*map(karesi , l))  

