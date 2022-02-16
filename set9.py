a = set([1, 2, 3])
b = set([2, 4, 6])
c = a.isdisjoint(b)#isdisjoint() metodunu kullanarak iki kümenin kesişim kümesinin boş olup olmadığı sorgulayabilirsiniz.
print(c)

d = set([1 , 2 , 3])
e = set([0 , 1 , 2 , 3 , 4 , 5])
f = d.issubset(e)#Yani bir kümenin, başka bir kümenin alt kümesi olup olmadığını bu metot yardımıyla öğrenebiliriz.
print(f)

g = set([1, 2, 3])
j = set([0 , 1 , 2 , 3 , 4 , 5])
k = j.issuperset(g)#“b kümesi a kümesini kapsar” ifadesini bu metotla gösteriyoruz.
print(k)

