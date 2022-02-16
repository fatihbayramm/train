a = "Bu bir Türkçe cümledir . "
a.encode("ascii" , errors="ignore")
print(a)

print("karakter dizisi\t")
print(repr("karakter dizisi\t"))

print(repr("İ"))
print(ascii("İ"))


# ord() Bu fonksiyon, bir karakterin sayı karşılığını verir:

print(ord("a"))

# chr() Bu fonksiyon, bir sayının karakter karşılığını verir:
print(chr(20))

