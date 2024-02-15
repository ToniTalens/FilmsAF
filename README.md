# FilmsAF
Aquest és el motlle amb el qual haureu de fer la vostra aplicació aplicant factoria abstracta

### Què conté el projecte?

El projecte conté inicialment tres arxius .py:

* Un arxiu anomenat pelicula.py, el qual conté la classe model. Algunes característiques:
  * El seu constructor (__init__) conté com atributs els mateixos que té la taula amb la qual es veu.
  * Conté un atribut anomenat **persistencia**, el qual com podrem comprovar, serà el "contenidor" que em permetrà persistir l'objecte a la base de dades (millor dit, persistir el valor dels atributs de l'objecte).
  * La id la fiquem com none, però a més no té setter. Recordeu que a la taula vam definir que aquest atribut fos autonumèric, per tant no es calcula per la lògica de programa sinó que ho fa el SGDB.

* Un arxiu anomenat ipersistencia_pelicula.py, el qual és la interfície amb els mètodes que em permeten fer el CRUD:
  * Aquest conté sols els mètodes totes (llegir tot de la taula), desa (per inserir un nou registre) i llegeix (per filtrar sols per títol o l'atribut que determinem).
  * Es pot completar amb tants mètodes abstractes com necessitem: per modificar, per esborrar, per fer consultes més complexes on hi ha altres taules, etc.

* Un arxiu anomenat persistencia_pelicula.py, el qual implementa la interfície ipersistencia_pelicula.py. A considerar:
  * Ha d'implementar tots els mètodes que té la interfície. Serà decissió nostra de disseny ficar o no lògica, és a dir, implementar codi per manipular les dades de les taules.
  * Pot perfectament contenir altres mètodes addicionals diferents als que marca la interfície, però això si, relacionats amb l'accés a les dades. Recordeu que preferiblement la lògica de negoci ha d'estar en altres classes o bé formar part del main.
  * Els mètodes utilitzen cursors (tal i com vam veure a la primera pràctica) amb els quals executen les queries sobre les taules (ja siguin selects, updates, inserts, etc. o siguin altres instruccions diferents per altres tipus de bases de dades).
  * Els mètodes que fan insert o update podrien no retornar res, però en aquest cas preferim que retornin l'objecte pel·lícula que manipulen.
  * El mètode totes retorna una llista, ja que al recòrrer tota la taula cal que vagi annexant pel·lícula a pel·lícula a una llista.
 

