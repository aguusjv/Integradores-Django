def mcd(x,y):
    resto = 0
    while(y > 0):
        resto = y
        y = x % y
        x = resto
    return x
resultado = (mcd(500,2560))
print(f"El maximo comun divisor es : {resultado} ")