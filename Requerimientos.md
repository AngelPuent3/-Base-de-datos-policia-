#  Base de datos Policia-
## Programacion Orientada a Objetos
### Proyecto escolar 2do-3er Parcial
La Policía quiere crear una base de datos sobre la seguridad en algunas entidades bancarias. Para ello
tiene en cuenta:

✅ Que cada entidad bancaria se caracteriza por un código y por el domicilio de su Central.
 
✅ Que cada entidad bancaria tiene más de una sucursal que también se caracteriza por un código y por
el domicilio, así como por el número de empleados de dicha sucursal.

✅ Que cada sucursal contrata, según el día, algunos vigilantes jurados, que se caracterizan por un
código y su edad. Un vigilante puede ser contratado por diferentes sucursales (incluso de diferentes
entidades), en distintas fechas y es un dato de interés dicha fecha, así como si se ha contratado con
arma o no.

✅ Por otra parte, se quiere controlar a las personas que han sido detenidas por atracar las sucursales de
dichas entidades. Estas personas se definen por una clave (código) y su nombre completo.

✅ Alguna de estas personas están integradas en algunas bandas organizadas y por ello se desea saber a
qué banda pertenecen, sin ser de interés si la banda ha participado en el delito o no Dichas bandas se
definen por un número de banda y por el número de miembros.

✅ Así mismo, es interesante saber en qué fecha ha atracado cada persona una sucursal. Evidentemente,
una persona puede atracar varias sucursales en diferentes fechas, así como que una sucursal puede
ser atracada por varias personas.

✅ Igualmente, se quiere saber qué Juez ha estado encargado del caso, sabiendo que un individuo, por
diferentes delitos, puede ser juzgado por diferentes jueces. Es de interés saber, en cada delito, si la
persona detenida ha sido condenada o no y de haberlo sido, cuánto tiempo pasará en la cárcel. Un
Juez se caracteriza por una clave interna del juzgado, su nombre y los años de servicio.

NOTA: En ningún caso interesa saber si un vigilante ha participado en la detención de un atracador
