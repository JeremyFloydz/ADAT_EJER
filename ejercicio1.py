import random

def rnd_word(fitxategi1, fitxategi2):
    # Abrir el archivo de lectura (fitxategi1) y el archivo de escritura (fitxategi2)
    with open(fitxategi1, 'r') as archivo1, open(fitxategi2, 'w') as archivo2:
        for linea in archivo1:
            # Dividir la línea en palabras
            palabras = linea.split()
            
            # Seleccionar una palabra aleatoria si la línea no está vacía
            if palabras:
                palabra_aleatoria = random.choice(palabras)
                # Escribir la palabra aleatoria en el segundo archivo
                archivo2.write(palabra_aleatoria + '\n')

# Ejemplo de uso
fitxategi1 = "archivo1.txt"
fitxategi2 = "archivo2.txt"
rnd_word(fitxategi1, fitxategi2)
