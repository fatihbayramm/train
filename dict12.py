lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu",
"üçüncü": "Adana Gençlerbirliği"}
print(lig)
print(lig["şampiyon"])
print(lig["ikinci"])
lig.clear()
print(lig)
del lig#del ile tamamen bellekten kaldırdır clear() metodu ile boş da olsa sözlük bellekte duruyordu.
print(lig)

print("-"*60)

