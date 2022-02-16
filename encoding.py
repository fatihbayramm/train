for i in range(128):
    if i % 4 == 0 :
        print("\n")

    print("{:<3}{:>8}\t".format(i , repr(chr(i))) , sep = "" , end ="")

for i in range (1 , 5):
    print("{} bayt kullanırsak toplam 2**{} = {}".format(i , i*8 , 2**(i*8)))