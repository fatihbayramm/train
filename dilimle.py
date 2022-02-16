kardiz = "on iki ada "
for kelime in kardiz.split():
    if kelime.startswith("i"):
        kelime = "İ" + kelime[1:]
    kelime = kelime.title()
    print(kelime , end=" ")    