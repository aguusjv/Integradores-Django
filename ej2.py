def mcm(x,y):
    if x > y:
        mayor = x
    else:
        mayor = y
    while (mayor % x != 0) or (mayor % y != 0):
        mayor += 1
    return mayor

resultado = print(mcm(24,36))
print("El resultado es: {resultado}")
