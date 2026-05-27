import matplotlib.pyplot as plt

def temperatura_promedio(temp):
  add = 0
  for i in range(len(temp)):
    add += temp[i]
  return add/len(temp)

def temperaturaMaximaYMinima(temp):
  min = 1000
  max = 0
  for i in range(len(temp)):
    if temp[i] < min:
      min = temp[i]
  for j in range(len(temp)):
    if temp[j] > max:
      max = temp[j]

  return min, max

def promedioDePrecipitaciones(precip):
  prom = 0
  for i in range(len(precip)):
    prom += precip[i]
  return prom/len(precip)

temp = []
precip = []

with open("../datos/data.csv", "r") as file:
    next(file)
    for line in file:
        varAux = line.strip().split(",")
        temp.append(float(varAux[0]))
        precip.append(float(varAux[1]))

temp_promedio = temperatura_promedio(temp)
temp_minima, temp_maxima = temperaturaMaximaYMinima(temp)
precip_promedio = promedioDePrecipitaciones(precip)

print(f"Temperatura promedio: {temp_promedio:.2f}, Temperatura minima: {temp_minima:.2f}, Temperatura maxima: {temp_maxima:.2f}, Precipitaciones promedio: {precip_promedio:.2f}")

