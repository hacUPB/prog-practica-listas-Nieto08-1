# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """
    suma= 0
    for filas in matriz:
        for dato in range(len(filas)):
            suma+= filas[dato]
    return suma

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """
    maximo = 0
    for i in matriz:
        for k in range(len(i)):
            maximo= max(maximo, i[k])
    return maximo

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    if n <2: 
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
        
# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    # matriz= [1,2,3],[6,4,2],[1,9,3]
    matriz_t= [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
    return (matriz_t)

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """
    #numeros= (1,2,3,4)
    pares= []
    for i in lista:
        if i%2== 0:
            pares.append(i)
    return (pares)

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    palabras= frase.split(" ")
    cnt_palabras= len(palabras)
    return (cnt_palabras) 
# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    tabla= [] 
    for cont in range(1,11):
        tabla.append(n*cont)
    return (tabla)
        


# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    cont_negas= 0
    lista= [12,15,-2,0,-5]
    for i in lista:
        if i < 0:
            cont_negas+= 1
    return (cont_negas) 

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    lista = [3, 5, 7, 9, 5]
    act = lista[0]
    ordenado = True
    for i in range(1, len(lista)):
        if(lista[i]<act):
            ordenado = False
            break
        act = lista[i]
    print(ordenado)
        
# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    letras = list(texto.upper().split(" "))
    cesar = ""
    for i in range(0, len(letras)):
        for k in range(0, len(letras[i])):
            ascii = ord(letras[i][k]) + desplazamiento    #obtiene el valor ascii de un caracter
            if(ascii > 90):
                ascii = 64 + (ascii - 90)          
            cesar+=chr(ascii)                             #convierte el valor ascii a un caracter
        cesar += " "
    return(cesar)

#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()