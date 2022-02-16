for i in range(256):
    print(i , bin(i)[2:] , hex(i)[2:])

a = [i for i in dir(int) if not i.startswith("_")]
print(a)    

sayi = 10
print(sayi.bit_length())
print((10).bit_length())

b = len(bin(10)[2:]) == (10).bit_length()
print(b)
#bit_length() metodu bir sayının ikili sistemde kaç bitlik yer kapladığını gösterir.
#bu bir tam sayı int() metotudur .