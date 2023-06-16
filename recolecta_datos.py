def ingresar_respuestas(evaluacion,numero_de_preguntas):
    archivo = open(evaluacion+".csv","w")
    linea1 = "Nombres,Apellidos,Rut,Curso"
    for p in range(numero_de_preguntas):
        linea1 = linea1 + ",P" + str(p+1)
    archivo.write(linea1+"\n")
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

def corregir(evaluacion):
    correctas =open(evaluacion+"_pauta.csv","r")
    linea_correctas = correctas.readlines()[0].rstrip("\n").split(",")
    correctas.close()
    resultados = open(evaluacion+".csv", "r")
    lineas = resultados.readlines()
    lista_alumnos_correccion = []
    for linea in lineas[1:]:
        lista_linea = linea.rstrip("\n").split(",")
        n_buenas = 0
        n_malas = 0
        n_omitidas = 0
        print(linea_correctas)
        print(lista_linea)
        for i in range(len(linea_correctas)):
            if linea_correctas[i] == lista_linea[i+4]:
                n_buenas = n_buenas + 1
            if lista_linea[i+4] == "":
                n_omitidas = n_omitidas + 1
        n_malas = len(linea_correctas)-n_buenas-n_omitidas
        correccion = ""
        for i in range(0,4):
            correccion = correccion + str(lista_linea[i]) + ","
        correccion = correccion + str(n_buenas) + "," + str(n_malas) + "," + str(n_omitidas)+"\n"
        lista_alumnos_correccion.append(correccion)
    resultados.close()
    resultados_alumnos = open(evaluacion+"_correccion.csv","w")
    resultados_alumnos.write("Nombres,Apellidos,Rut,Curso,Buenas,Malas,Omitidas\n")
    for alumno in lista_alumnos_correccion:
        resultados_alumnos.write(alumno)
    resultados_alumnos.close()


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
    corregir(evaluacion)
    
