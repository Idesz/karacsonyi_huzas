import random
class test:
_eredmeny: list[eredmeny] = []

def kalap_huzas(lista):
    if not lista:
        return []

    maradek = _eredmeny
    kezdo = random.choice(maradek)
    lanc = [kezdo]
    maradek.remove(kezdo)

    while maradek:
        kov = random.choice(maradek)
        lanc.append(kov)
        maradek.remove(kov)

    return lanc