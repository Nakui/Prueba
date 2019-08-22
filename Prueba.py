#Task1
print("Ingrese una cantidad de Quetzales")
solicitado = int(input(""))



cincuenta = solicitado / 5
cincuentaa = solicitado % 5
veitycinco = cincuentaa/ 0.25
veitycincoo = cincuentaa % 0.25
diez = veitycincoo / 0.10
diezz = veitycincoo % 0.10
cinco = diezz / 0.5

if solicitado // 5 == 1:
    print("Valor no aceptado")
else:
    print("Cambio")
    print(int(cincuenta), "monedas","50C")
    print(int(veitycinco),"monedas","25C")
    print(int(diez),"monedas","10C")
    print(int(cinco),"monedas","5C")


"""------------------------------------------"""

#Task2
def Task2(numero):
    suma = 0
    cifra = 0

    #return msj
    
    a = int(str(numero)[:: -1])

    suma += a + numero
    
    return suma

   
        

