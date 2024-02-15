#!/bin/usr/python3

from ipersistencia_pelicula import IPersistencia_pelicula
from pelicula import Pelicula
from typing  import List
import mysql.connector
import logging

class Persistencia_pelicula_mysql(IPersistencia_pelicula):
    def __init__(self, credencials) -> None:
        self._credencials = credencials
        self._conn = mysql.connector.connect(
                host=credencials["host"],
                user=credencials["user"],
                password=credencials["password"],
                database=credencials["database"]
                )
        if not self.check_table():
            self.create_table()

    def check_table(self):
        try:
            cursor = self._conn.cursor(buffered=True)
            cursor.execute("SELECT * FROM PELICULA;")
            cursor.reset()
        except mysql.connector.errors.ProgrammingError:
            return False
        return True
    
    def totes(self) -> List[Pelicula]:
        cursor = self._conn.cursor(buffered=True)
        query = "select id, titulo, anyo, puntuacion, votos from PELICULA;"
        cursor.execute(query)
        registres = cursor.fetchall()
        cursor.reset()
        resultat = []
        for registre in registres:
            pelicula = Pelicula(registre[1],registre[2],registre[3],registre[4],self,registre[0])
            resultat.append(pelicula)
        return resultat
    
    def desa(self,pelicula:Pelicula) -> Pelicula:
        cursor = self._conn.cursor(buffered=True)
        query = "insert into PELICULA (titulo,anyo,puntuacion,votos) values (%s,%s,%s,%s);"
        parameters = (pelicula.titol,pelicula.any,pelicula.puntuacio,pelicula.vots)
        try:
            cursor.execute(query,parameters)
            nova_id = cursor.lastrowid
            logging.info(f"[Persistencia] Nova pelicula amb id = {nova_id}.")
            self._conn.commit() 
        except mysql.connector.errors.IntegrityError:
            logging.info("[Persistencia] Integrity error escrivint pelicula.")
        return self.llegeix(pelicula.titol)
    
    def llegeix(self, titol: str) -> Pelicula:
        cursor = self._conn.cursor(buffered=True)
        query = "select id, titulo, anyo, puntuacion, votos from PELICULA where titulo = %s;"
        parametres = (titol,)
        cursor.execute(query, parametres)
        registre = cursor.fetchone()
        cursor.reset()
        if registre is None:
            logging.info(f"[Persistencia] pelicula inexistent {titol}.")
            return None
        resultat = Pelicula(registre[1],registre[2],registre[3],registre[4],self,registre[0])
        logging.info(f"[Persistencia] Trobada pelicula {titol}.")
        return resultat

if __name__ == "__main__":
    logging.basicConfig(filename='pelicules.log', encoding='utf-8', level=logging.DEBUG)
    credencials = {
        "host" : "localhost",
        "user" : "dam_app",
        "password" : "1234",
        "database" : "pelis"
        }
    
    pers_pelis = Persistencia_pelicula_mysql(credencials)
#    print(pers_pelis.totes())
    p = Pelicula("La sociedad sin nieve",2023,5.0,10000,pers_pelis)
    p.persistencia.desa(p)
