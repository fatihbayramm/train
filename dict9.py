sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sozluk.keys())       
print(sozluk.values())   
liste = list(sozluk.keys())
print(liste)
demet = tuple(sozluk.values())
print(demet)
kardiz = " , ".join(sozluk.keys())
print(kardiz)

kardiz2 = " , ".join([str(i) for i in sozluk.values()])
print(kardiz2)