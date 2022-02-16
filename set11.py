a = set([1,2, 5])
b = set([1,4, 5])
a.symmetric_difference_update(b)
print(a)
#Gördüğünüz gibi, a kümesinin eski öğeleri gitti, yerlerine symmetric_difference() metoduyla elde edilen çıktı geldi.
# Yani a kümesi, symmetric_difference() metodunun sonucuna göre güncellenmiş oldu…

c = set(["elma", "armut", "kebap"])
print(c.pop())#rastgele birini siliyor . silineni ekrana veriyor .

dondurulmus = frozenset(["elma", "armut", "ayva"])
#Eğer öğeleri üzerinde değişiklik yapılamayan bir küme oluşturmak isterseniz
# set() yerine frozenset() fonksiyonunu kullanabilirsiniz.
print(dir(dondurulmus))
