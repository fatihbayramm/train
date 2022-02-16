#abs() bir sayının mutlak değerini verir.
print(abs(-20))
print(abs(1))
print(abs(20.0))
print(abs(20+3j))

#round() fonksiyonu bir sayıyı belli ölçütlere göre yukarı veya aşağı doğru yuvarlamamızı sağlar.
a = [round(12.4) , round(11.2)]
print(a)
b = [round(1.5) , round(12.5)]
print(b)
#Gördüğünüz gibi, fonksiyonumuz 1.5 sayısını yukarı doğru, 12.5 sayısını ise aşağı doğru yuvarladı.
#Bunun sebebi, kayan noktalı bir sayının üst ve alt tam sayılara olan uzaklığının birbirine eşit olduğu durumlarda
#Python’ın çift sayıya doğru yuvarlama yapmayı tercih etmesidir.

c = [round(22/7 , 2) , round(22/7 , 3) , round(22/7 , 1)]
print(c)
#yuvarlama hassasiyeti virgülden sonra kaç basamağın gozukeceğini ayarlar .