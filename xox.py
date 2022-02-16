tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*15)

for i in tahta:
    print("\t".expandtabs(30) , *i , end ="\n"*2)

kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

sira = 1
while True:
    if sira % 2 == 0 :
        isaret = "X".center(3)
    else:
        isaret = "O".center(3)
    sira += 1
    print()
    print("İŞARET:{}\n".format(isaret))
    x = input("Yukarıdan aşağıya [1 , 2 , 3] :".ljust(30))
    if x == "q" :
        print("Oyundan çıkılıyor...")
        break
    y = input("Soldan sağa [1 , 2 , 3] :".ljust(30))
    if y == "q" :
        print("Oyundan çıkılıyor...")
        break

    x = int(x) -1
    y = int(y) -1    

    print("\n" * 15)
    if tahta[x][y] == "___":
        tahta[x][y] = isaret
        if isaret == "X".center(3):
            x_durumu += [[x , y]]
        elif isaret == "O".center(3):
            o_durumu += [[x , y]]
        sira += 1
    else:
        print("\nORASI DOLU ! TEKRAR DENEYİN\n")   
for i in tahta:
    print("\t".expandtabs(30) , *i , end="\n" * 2)
for i in kazanma_olcutleri:
    o = [z for z in i if z in o_durumu]
    x = [z for z in i if z in x_durumu]
    if len(o) == len(i):
        print("O KAZANDI !")
        quit()
    if len(x) == len(i):
        print("X KAZANDI ! ")
        quit()    


