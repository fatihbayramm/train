k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.difference_update(k2)#Bu metot, difference() metodundan elde edilen sonuca göre bir kümenin güncellenmesini sağlar.
print(k1)

hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
hayvanlar.discard("kedi")
hayvanlar.discard("öküz")
hayvanlar.remove("at")
#discard metodunda olmayan bir öğeyi silmeye çalışırken hata almıyorduk ama remove da alıyoruz .
print(hayvanlar)