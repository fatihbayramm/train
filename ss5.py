a = [i for i in dir(complex) if not i.startswith("_")]
print(a)

c = 12+4j
print(c.imag) # imag adlı nitelik, bize bir karmaşık sayının sanal kısmını verir
print(c.real) #real adlı nitelik bize bir karmaşık sayının gerçek kısmını verir