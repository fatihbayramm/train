b = bytes("ş" , "utf-8")
print(b)

a = bytes("Fırat" , "ascii" , errors = "replace")
print(a)

for i in dir(bytes):
    if i not in dir(""):
        print(i)