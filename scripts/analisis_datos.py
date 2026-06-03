import matplotlib.pyplot as plt       #importar libreria para graficos

def temperatura_promedio(temp):
  add = 0                             #add: acumula las temperturas y luego las divide por la cantidad de las mismas
  for i in range(len(temp)):
    add += temp[i]
  return add/len(temp)

def temperatura_maxima_minima(temp):
  min = 1000
  max = 0
  for i in range(len(temp)):
    if temp[i] < min:
      min = temp[i]
  for j in range(len(temp)):
    if temp[j] > max:
      max = temp[j]                  #compara el numero actual de la lista con el anterior mas bajo o mas alto para determinar si es mayor o menor

  return min, max

def promedio_precipitaciones(precip):
  prom = 0
  for i in range(len(precip)):
    prom += precip[i]
  return prom/len(precip)           #prom: acumula las precipitaciones y luego las divide por la cantidad de las mismas

temp = []
precip = []

with open("../datos/data.csv", "r") as file:      #"r otorga permisos de lectura al archivo"
    next(file)
    for line in file:
        varAux = line.strip().split(",")
        temp.append(float(varAux[0]))
        precip.append(float(varAux[1]))           #se recorre el archivo linea por linea guardando cada linea, ordenada

temp_promedio = temperatura_promedio(temp)
temp_minima, temp_maxima = temperatura_maxima_minima(temp)
precip_promedio = promedio_precipitaciones(precip)

print(f"Temperatura promedio: {temp_promedio:.2f}, Temperatura minima: {temp_minima:.2f}, Temperatura maxima: {temp_maxima:.2f}, Precipitaciones promedio: {precip_promedio:.2f}")

with open("../resultados/resultados.csv", "w") as file:
    file.write("temperatura promedio,temperatura minima,temperatura maxima,precipitaciones promedio \n")          #Escribe los archivos y da formato
    file.write(f"{temp_promedio:.2f},{temp_minima:.2f},{temp_maxima:.2f},{precip_promedio:.2f}")

plt.plot(temp)
plt.title("Grafico de temperatura")
plt.xlabel("Dias")
plt.ylabel("Temperatura")
plt.savefig("../resultados/temperatura.png")  #guarda la imagen del cuadro creado.
plt.show()
