import csv

def liderTabla(equipos):
    return 0
def CalcularPuntos(equipos):
    return 0



dictEquipos = {}
with open("input/equiposChampions.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)
        dictEquipos[fila["equipo"]] = {
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"])
            }
for equipo in dictEquipos:
    print(equipo["ganados"])


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