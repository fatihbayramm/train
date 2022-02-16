#baytları belli bir kodlama biçimine göre karakter dizilerine dönüştürebilmek için decode() metodundan yararlanacağız
a = b"\xc4\xb0".decode("utf-8")
print(a)

b = b"\xc4\xb0".decode("cp1254")
print(b)

#Bu metot, onaltılı sayma sistemindeki bir sayıdan oluşan bir karakter dizisini alıp, bayta dönüştürür.

c = bytes.fromhex("c4b0")
print(c)