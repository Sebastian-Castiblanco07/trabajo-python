import csv

def liderTabla(equipos): #en realidad es organizar por orden de puntos pero el ejercicio pedia que se llamara asi
   
   
    return 0
def CalcularPuntos(equipo):
    return equipo["ganados"]*3 + equipo["empatados"]*1



dictEquipos = {}
with open("input/equiposChampions.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        
        dictEquipos[fila["equipo"]] = {
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor": int(fila["goles_favor"]),
            "goles_contra": int(fila["goles_contra"])
            }
for equipo in dictEquipos:
    dictEquipos[equipo]["puntos"] = CalcularPuntos(dictEquipos[equipo])

print(dictEquipos)
"""
with open("output/equiposSalida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(
        ["nombre", "ganados", "empatados", "perdidos"]
    )

    for key, value in dictEquipos.items():
        print(key, value)
        escritor.writerow(
            [key, value["ganados"], value["empatados"], value["perdidos"]]
        )
        """