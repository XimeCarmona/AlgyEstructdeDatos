#función recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras.

vector=['casa', 'flor', 'mariposa', 'flor', 'auto', 'mariposa', 'flor']
cont=0
palabra='flor'

def palabra_repetida(vector, palabra):
    if len(vector)==0:
        return 0

    elif vector[0] == palabra:
        return 1 + palabra_repetida(vector[1:], palabra)
    else:
        return palabra_repetida(vector[1:], palabra)

cont = palabra_repetida(vector, 'flor')
print('Se encontro', cont, 'veces la palabra flor')





#def palabra_repetida(palabra, vector, indice=0, contador=0):
    # Caso base: si se recorrió todo el vector, se devuelve el contador
#    if indice == len(vector):
#        return contador

    # Si la palabra actual coincide con la palabra buscada, se incrementa el contador
#    if vector[indice] == palabra:
#        contador += 1

    # Se llama recursivamente a la función para el siguiente índice del vector
#    return palabra_repetida(palabra, vector, indice + 1, contador)
    