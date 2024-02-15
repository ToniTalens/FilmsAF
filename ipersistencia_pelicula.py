from abc import ABC, abstractclassmethod
from pelicula import Pelicula
from typing import List

class IPersistencia_pelicula(ABC):
    @abstractclassmethod
    def totes(self) -> List[Pelicula]:
        pass
    
    @abstractclassmethod
    def desa(self, pelicula: Pelicula) -> Pelicula:
        pass

#    @abstractclassmethod
#    def llegeix(self, nom: str) -> Pelicula:
#        pass