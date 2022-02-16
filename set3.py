import random
liste = [random.randint(0 , 1000) for i in range(1000)]
kume = {i for i in liste  if i < 100}
print(kume)