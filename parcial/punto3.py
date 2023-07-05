class Cazarrecompensas():
    def init(self, planeta_visitado, capturado, recompensa):
        self.__planeta_visitado = planeta_visitado
        self.__capturado = capturado
        self.__recompensa = recompensa

pila_cazarrecompensa= [
    {'planeta_visitado': 'planeta1', 'capturado': 'capturado1', 'recompensa': 4000 },
    {'planeta_visitado': 'planeta2', 'capturado': 'capturado2', 'recompensa': 7250 },
    {'planeta_visitado': 'planeta3', 'capturado': 'Han Solo', 'recompensa': 13000 },
    {'planeta_visitado': 'planeta4', 'capturado': 'capturado3', 'recompensa': 2500 },
    ]    
#a. Mostrar los planetas visitados en el orden hizo las misiones.

pila_auxiliar = []

# Desapilar elementos de la pila original y agregarlos a la pila auxiliar
while pila_cazarrecompensa:
    elemento_desapilado = pila_cazarrecompensa.pop()
    pila_auxiliar.append(elemento_desapilado)
print('Planetas visitados en orden')
print(pila_auxiliar)
for elemento in pila_auxiliar:
    print(elemento)
    
#b. Determinar cuántos créditos galácticos recaudo en total.

credito_recaudado = 0

for cazarrecompensas in pila_auxiliar:
    recompensas = cazarrecompensas['recompensa']
    credito_recaudado = credito_recaudado + recompensas

print("El total de créditos recaudados es:", credito_recaudado)

#c. Determinar el número de la misión en que capturo a Han Solo y en que planeta fue, suponga que dicha misión está cargada.

han_solo = 0
planeta_han_solo = 0

for i, mision in enumerate(pila_auxiliar):
    if mision['capturado'] == 'Han Solo':
        han_solo = i + 1
        planeta_han_solo = mision['planeta_visitado']
        break

if han_solo is not 0:
    print("Han Solo fue capturado en la misión número:", han_solo)
    print("La captura ocurrió en el planeta:", planeta_han_solo)
else:
    print("Han Solo no fue capturado en ninguna misión")