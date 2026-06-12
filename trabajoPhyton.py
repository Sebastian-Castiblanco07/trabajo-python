import csv

def liderTabla(equipos): #en realidad es organizar por orden de puntos pero el ejercicio pedia que se llamara asi
    equiposOrdenados = sorted(equipos.items(), key=lambda x: CalcularPuntos(x[1]), reverse=True)
    return dict(equiposOrdenados)
   
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
    dictEquipos[equipo]["diferencia_goles"] = dictEquipos[equipo]["goles_favor"] - dictEquipos[equipo]["goles_contra"]

dictEquipos = liderTabla(dictEquipos)
print("\n############## el ganador es: ##############\n")
print(list(dictEquipos.keys())[0])
print("\n","P.D: los partidos ganados, empatados y perdidos, al igual que los puntos y la diferencia de goles de cada equipo fueron impresos en orden dentro de 'equiposSalida.csv' dentro de la carpeta output")

with open("output/equiposSalida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(
        ["nombre", "ganados", "empatados", "perdidos","goles_favor","goles_contra","puntos","diferencia_goles"]
    )

    for key, value in dictEquipos.items():
        escritor.writerow(
            [key, value["ganados"], value["empatados"], value["perdidos"], value["goles_favor"],value["goles_contra"],value["puntos"],value["diferencia_goles"]]
        )
        