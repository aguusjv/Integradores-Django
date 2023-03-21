def contador_palabras(string):
    # Remove punctuation and convert to lowercase
    remove = string.lower().replace(',', '').replace('.', '')
    
    # Split the string into words
    palabras = remove.split()
    
    # Count the frequency of each word
    palabra_frecuencia = {}
    for palabra in palabras:
        if palabra in palabra_frecuencia:
            palabra_frecuencia[palabra] += 1
        else:
            palabra_frecuencia[palabra] = 1
            
    return palabra_frecuencia

def palabraMasRepe(palabra_frecuencia):
    # Initialize variables for the most common word and its frequency
    mas_repetida = None
    mas_frecuente = 0
    
    # Find the most common word and its frequency
    for palabra in palabra_frecuencia:
        frecuencia = palabra_frecuencia[palabra]
        if frecuencia > mas_frecuente:
            mas_repetida = palabra
            mas_frecuente = frecuencia
            
    return (mas_repetida, mas_frecuente)
    
# Example usage:
texto = input("Ingrese su texto: ")
palabra_frecuencia = contador_palabras(texto)
mas_repetida = palabraMasRepe(palabra_frecuencia)
print(mas_repetida)
