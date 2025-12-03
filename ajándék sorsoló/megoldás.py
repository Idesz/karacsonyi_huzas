from eredmény import eredmeny
import random
import os


class megoldas:
    _eredmeny: list[eredmeny] = []

    def __init__(self, állomány_neve: str = None) -> None:
        if állomány_neve is None:
            állomány_neve = os.path.join(os.path.dirname(__file__), "10A_nevsor.txt")

        self._eredmeny: list[eredmeny] = []
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:
                sor = sor.strip()
                if sor:
                    új_eredmény: eredmeny = eredmeny(sor)
                    self._eredmeny.append(új_eredmény)

    def tanuló_keresése(self, név: str) -> str:
        vissza: str = "\tEbbe az osztályba jár a tanuló"
        tanuló: eredmeny | None = self.keres_Tanuló(név)
        if tanuló is None:
            vissza += " Nem ebbe az osztályba jár"
        else:
            vissza += f" tanuló sorszáma: {tanuló.sorszám}, tanuló neve: {tanuló.Tanuló_neve}, tanuló emailje: {tanuló.Tanuló_email}."
        return vissza

    def keres_Tanuló(self, név: str) -> eredmeny | None:
        név_norm = név.strip()
        for e in self._eredmeny:
            e_nev = getattr(e, "Tanuló_neve", "") or getattr(e, "név", "")
            if e_nev.strip() == név_norm:
                return e
        return None

    def kalap_huzas(self):
        if not self._eredmeny:
            return []

        maradek = self._eredmeny[:]
        kezdo = random.choice(maradek)
        lanc = [kezdo]
        maradek.remove(kezdo)

        while maradek:
            kov = random.choice(maradek)
            lanc.append(kov)
            maradek.remove(kov)

        return lanc

    def vegrehajtas_huzas(self):
        lanc = self.kalap_huzas()
        parok = []
        for i in range(len(lanc)):
            huzo = lanc[i]
            huzott = lanc[(i + 1) % len(lanc)]
            parok.append((huzo, huzott))
        return parok
