a = [i for i in dir(float) if not i.startswith("_")]
print(a)

sayi = 4.5
c = sayi.as_integer_ratio()#hangi sayılarını birbirine bölersem 4.5 sonucunu elde ederim ?
print(c)

b = (12.0).is_integer()
print(b)

d = (12.5).is_integer()
print(d)