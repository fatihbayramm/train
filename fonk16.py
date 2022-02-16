#chr () Bu fonksiyon, kendisine parametre olarak verilen bir tam sayının karakter karşılığını döndürür.
print(chr(65))
print(ascii(chr(10)))
print(chr(305))



s = set("istihza")
df = frozenset(s)
print(df)


a = int("4cf" , 16)#burada 16lık sayma sis. 4cf sayısını onlu sistemdeki karşılığına çeviriyor .
print(a)

bayt = b"istihza"
a = str(bayt , encoding = "utf-8")
print(a)

bayt2 = bytes("kadın" , encoding = "utf-8")
kardiz = str(bayt2 , encoding = "ascii" , errors = "ignore")
print(kardiz)