def ingresar_respuestas(evaluacion,numero_de_preguntas):
    archivo = open(evaluacion+".csv","w")

    iniciar = input("Añadir alumnos?(S/N) -> ")
    while iniciar.lower()=="s": 
        nombres = input("Nombres: ")
        apellidos = input("Apellidos: ")
        rut = input("RUT: ")
        curso = input("Curso: ")
        datos=nombres+","+apellidos+","+rut+","+curso
        lista_respuestas = []
        for i in range(numero_de_preguntas):
            respuesta = input(str(i+1)+". -> ")
            if respuesta == "0":
                num = int(input("Ingresa el número de la pregunta que quieres corregir: "))
                res = input(str(num)+". -> ")
                print("En la pregunta", num, "has cambiado la respuesta", lista_respuestas[num-1], "por la respuesta",res+".")
                lista_respuestas = corregir_respuesta(lista_respuestas,num,res)
                respuesta = input(str(i+1)+". -> ")
            lista_respuestas.append(respuesta)
            
        for res in lista_respuestas:
            datos=datos+","+res
        archivo.write(datos+"\n")
        iniciar = input("Ingresar otro alumno?(S/N) -> ")
    archivo.close()

def corregir_respuesta(lista, numero_pregunta,alternativa_correcta):
    lista[numero_pregunta-1]=alternativa_correcta
    return lista


def crear_pauta(numero_de_preguntas):
    respuestas=""
    print("A continuación ingresa las respuestas correctas de los",numero_de_preguntas,"ejercicios.")
    print()
    for i in range(numero_de_preguntas):
        respuesta = input(str(i+1)+". -> ")
        if i == 0:
            respuestas = respuesta
        else:
            respuestas = respuestas + "," + respuesta
    print()
    print("Ya has ingresado todas las respuestas de la pauta, bien hecho!")
    print()
    archivo = open(evaluacion+"_pauta.csv","w")
    archivo.write(respuestas+"\n")
    archivo.close()
    print("La pauta se ha creado correctamente.")

evaluacion = input("Qué evaluación es esta? -> ")
numero_de_preguntas = int(input("Número de preguntas: "))

respuesta = input("Deseas comenzar a ingresar las respuestas?(S/N) -> ")
if respuesta.lower()=="s":
    print("Primero creemos la pauta.")
    print()
    crear_pauta(numero_de_preguntas)
    print("Ahora, comencemos con el ingreso de los estudantes.")
    print()
    ingresar_respuestas(evaluacion,numero_de_preguntas)
    
