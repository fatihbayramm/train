def fibonacci():
    x = 1
    y = 0
    z = 0
    while not x > 100 :
        z = y
        y = x
        x = y + z
        yield x
        

a = fibonacci()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print("-"*30)

for i in fibonacci():
    print(i)
