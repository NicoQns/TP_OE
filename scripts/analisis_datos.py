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
