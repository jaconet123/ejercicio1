print("Sistema de parqueo")
sw=1
dia= str (input("ingrese dia de la seamana, escriba nombre del dia completo")).lower()
horas=int (input("ingrese cantidad de horas que paso en el parqueo"))
minut=int (input("ingrese cantidad de minutos que paso en el parqueo"))

valor=0
if minut<0 and horas<0 :
    print("cantidad de tiempono valida,  alguna debe ser mayor a 0")
else:
    if dia=="lunes" or dia=="martes" or dia=="miercoles":
        valor=2
    elif dia=="jueves" or dia=="viernes":
        valor=2.50
        
    elif dia=="sabado" or dia=="domingo":
        valor=3
        
    else:
        print("dia no valido")
        sw=0
if sw==1:
    if minut>=5:
        horas=horas+1
    print("El valor a pagar es ",horas*valor) 
#soy un comentario
    
