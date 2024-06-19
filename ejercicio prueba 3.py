import csv
def imprimir_lista(busc,listita):
    encontrado=False  
    for x in listita:
        if busc==int(x['camiseta']):
            print ("Camiseta :",x['camiseta'],"Nombre :",x['nombre'],"Goles :",x['goles'],"calificar:",x["calificar"])
            encontrado=True
            break
    if encontrado==False:
        print("No existe ")
def confirmar():
    resp=input("¿Esta seguro de querer eliminarlo (si/no):?").lower()
    if resp==("si"):
        return True
    else :
        return False    
def eliminar(id_e,listita):
    for x in listita :
            if id_e==int(x['camiseta']):
                print("Datos del jugador: \n")
                print (x)
                print("")
                r=confirmar()
                if r:
                    listita.remove(x)
                    print("Elemento eliminado correctamente .")
                else:
                    print("Eliminacion cancelada.")
                break
def calificacion(gol):
    if gol>=1 and gol<=5:
        cal="Amateur"
    elif gol>=6 and gol<=15:
        cal="Semi"
    elif gol>16:
        cal="Pro"
    return(cal) 
def promedio():
    acum=0
    cant=len(lista)
    if cant>0:
        for x in lista:
            acum=acum+int(x['goles'])
        prom=acum/cant
        print("Goles acumulados : ", acum)
        print("Goles Promedio :",prom)
    else :
        print("no hay jugador agregado")

def mayor():
    mayor=0
    for x in lista:
        if int(x['goles'])>int(mayor):
            mayor = x['goles']
        else:
            mayor=mayor
    print("El mayor es: ", mayor)
lista=[]
diccionario={}
while True:
    print ("")
    print (".-.-.-.-.M E N U   J U G A D O R E S-.-.-.-.-")
    print ("1-Agregar jugador ")
    print ("2-Listar jugadores")
    print ("3-Imprimir datos de jugador")
    print ("4-Eliminar jugador")
    print ("5-Estadísticas")
    print ("6-Cargar base de datos")
    print ("7-Cargar datos desde archivo")
    print ("0-Salir")
    print ("")
    op=int(input("Ingrese una opción :\n"))
    if op==1:
        print ("")
        camiseta=int(input("ingrese numero de camiseta : \n"))
        nombre=input("ingrese nombre :\n")
        goles=int(input("ingrese goles :\n"))
        calificar=calificacion(goles)
        diccionario={'camiseta':camiseta,'nombre':nombre,'goles':goles,'calificar':calificar}
        lista.append(diccionario)
    elif op==2:
        print ("")
        print("-.-.-.-..L I S T A  D E  J U G A D O R E S  .-.-.-.-.-")
        for x in lista:
            print("camiseta :",x["camiseta"],"nombre :",x["nombre"],"goles :",x["goles"],"calificar:",x["calificar"])

    elif op==3:
        print("")
        buscar=int(input("ingrese n° camiseta a buscar:\n"))
        imprimir_lista(buscar,lista)
                
    elif op==4:
        elim=int(input("Ingrese n° de camiseta a elimina:\n"))        
        eliminar(elim,lista)
        print ("")
    elif op==5:
        print ("")
        promedio()
        mayor()
    elif op==6:
        print ("")
        with open ('bbdd.csv','w',newline='') as bbdd:
            campo=['camiseta','nombre','goles','calificar']
            escritor=csv.DictWriter(bbdd,fieldnames=campo)
            escritor.writeheader()
            escritor.writerows(lista)
    elif op==7:
        print ("")
        with open ('bbdd.csv','r',newline='') as bbdd:
            lector=csv.DictReader(bbdd)
            for fila in lector:
                lista.append(fila)
    elif op==0:
        print ("")
        print ("Saliendo...")
    else:
        print ("Ingrese una opcion valida")