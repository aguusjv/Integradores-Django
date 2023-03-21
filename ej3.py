def creador_dicc(cadena):
    listaPalabras = cadena.split()

    frecuenciaPalab = []
    for i in listaPalabras:
        frecuenciaPalab.append(listaPalabras.count(i))
    print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

texto = input("Ingrese su cadena: ")
creador_dicc(texto)
