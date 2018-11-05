import csv

file = open("televidentes_canal_horario.csv", 'r')  # read only

reader = csv.reader(file)

t0values = []

for row in reader:
    aux = []
    for i in range(0,9):
        aux.append(int(row[i]))
        t0values.append(aux)
    print(aux)
    print("---------------------------lol")
print(t0values)

espectadores = t0values

def createCsv(espectadores, time):
    file = open("rungeKutta/t"+ str(time)+".csv", "w")
    for i in range(0, 6):
        file.write("{0:.2f}".format(espectadores[i]) + "\n")

for time in range(1, 11):
    newEspectadores = []

    wall = []
    for i in range(0, 22):
        wall.append(15)

    newEspectadores.append(wall)
    for i in range(1,21):
        aux = []
        aux.append(15)
        for j in range(1,21):
            # ambTemp = ambientTemp(i,j, prevTemp)
            # temp = analyticSolution(10, prevTemp[i][j], ambTemp)
            # temp = rk4(0, prevTemp[i][j],ambTemp,10,1)
            # aux.append(temp)
        aux.append(15)
        newEspectadores.append(aux)

    newEspectadores.append(wall)
    createCsv(newEspectadores, time)
    prevTemp = newEspectadores