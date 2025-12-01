class eredmeny:
    _sorszám: int
    _Tanuló_neve: str
    _Tanuló_email: str

    @property
    def Tanuló_neve(self) -> str:
        return self._Tanuló_neve

    @property
    def Tanuló_email(self) -> str:
        return self._Tanuló_email

    @property
    def sorszám(self) -> int:
        return self._sorszám

    @property
    def tanuló_adatai(self) -> str:
        return f"{self._sorszám} {self._Tanuló_neve} {self._Tanuló_email}"

    def __init__(self, adatsor: str) -> None:
        Ssz, Tn, Te = adatsor.split(";")
        self._Tanuló_neve = Tn
        self._sorszám = int(Ssz)
        self._Tanuló_email = Te


# Module-level variables for import (will be set at runtime)
húzó = None
húzott = None
Tanuló_email = None
