#Debemos crear una función que verifique si un número es primo.Otra función que cuente la cantidad de números primos dentro de una lista dada.
#Un main que integre estas funciones y muestre los resultados.
def es_primo(numero):#Creamos una función para saber si el número es primo.
    if numero < 2: #si número es menor a 2
        return False #retorna falso porque los números menores a 2 no son considerados primos.
    for i in range(2, int(numero ** 0.5) + 1): # creamos un for para recorrer desde 2 hasta la raíz cuadrada del número ingresado.
     if numero % i == 0: #si el resto de dividir numero entre i es igual a 0 significa que número no es primo.
        return False # por lo tanto devuelve falso
    return True # si el for no encuentra ningún divisor, significa que el número es primo.Devuelve true.
def contar_primos(lista_numeros):#Definimos la función "contar_primos" que toma un argumento "lista_numeros".
    contador = 0 #iniciamos contador en 0 para contar la cantidad de números primos de la lista.
    for numero in lista_numeros: #for para recorrer la lista
        if es_primo(numero):# usamos la función creada "es_primo" para verificar. 
            contador += 1 # si es primo incrementa contador en 1
    return contador #cuando termina el bucle devuelve el valor de contador.
def main(): # Definimos la función main() que es el punto de entrada del programa.
    lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()] #pedimos al usuario que introduzca una lista de números separados por espacios.
    #input() recibe la entrada como cadena de texto,.split divide la cadena en partes individuales separadas por espacios, int(x) for x in.. es una comprensión de listas que convierte cada uno
    #de esos fragmentos en un número entero ("int") y lo guarda en la "lista".
    cantidad_primos = contar_primos(lista) #llamamos a la función contar primos pasando la lista ingresada por el usuario.El resultado se almacena en "cantidad_primos".
    print(f"La cantidad de números primos en la lista es: {cantidad_primos}") #mostramos el resultado.
if __name__ == "__main__":
    main()
    """ Esta última línea es una comprobación en los programas de Python. Verifica si el script está siendo ejecutado directamente (es decir, no está siendo importado como módulo en otro script)
    Si el script se está ejecutando directamente se llama a la función main(). Los script son archivos que contienen códigos que se ejecutan desde la línea de comandos o desde otro script
    En otras palabras, cualquier código dentro de este bloque solo se ejecutará si el archivo se ejecuta directamente. Si el archivo se importa, el código dentro de este bloque se ingnorará.
    Esto es útil para escribir código que puede ser utilizado tanto como un módulo importado en otos programas, como un script independiente"""
