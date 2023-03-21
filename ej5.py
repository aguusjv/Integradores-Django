
def valorEnteroIterado():
    while True:
        try: 
            valor = int(input("Ingrese un numero: "))  
            break
        except:    
            print("El valor ingresado no es un entero")
valorEnteroIterado()        
        
def valorEnteroRecursivo():
    try: 
        valor = int(input("Ingrese un numero: "))  
    except:    
        print("El valor ingresado no es un entero")
        valorEnteroRecursivo()
valorEnteroRecursivo()