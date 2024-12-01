from Funciones import *

def menu_competencia():
    participantes_ingresados = crear_array_bidimensional(5,6)
    notas_cargadas = False
    salir = True
    while(salir):
        print("*Competencia de cocina*\n1.Cargar votos de los participantes.\n2.Mostrar Votos.\n3.Ordenar votos por nota promedio.\n4.3 Peores votos.\n5.Mayores promedios.\n6.Jurado/s malo/s.\n7.Sumatoria.\n8.Definir Ganador.\n9.Salir\n")

        opcion = int(input("Ingrese su opcion: "))
        while opcion < 1 or opcion > 9:
            opcion = int(input("Ingrese nuevamente su opcion(debe ser entre 1 y 9): "))
            
        if opcion == 1:
            participantes_ingresados = cargar_notas_participantes(participantes_ingresados)
            notas_cargadas = True
        elif notas_cargadas:
            if opcion == 2:
                mostrar_notas(participantes_ingresados,5)
            elif opcion == 3:
                orden_ingresada = input("Ingrese en que orden quiere hacerlo Menor a mayor(ingrese asc) o Mayor a menor(desc):")
                participantes_ingresados = ordenar_votos_burbuja(participantes_ingresados,orden_ingresada)
                print("Se ordenaron los participantes por promedio de votos")
            elif opcion == 4:
                mostrar_tres_peores_promedios(participantes_ingresados)
            elif opcion == 5:
                mayores_promedios(participantes_ingresados)
            elif opcion == 6:
                jurado_malo(participantes_ingresados)
            elif opcion == 7:
                sumatoria(participantes_ingresados)
            elif opcion == 8:
                definir_ganador(participantes_ingresados)
            elif opcion == 9:
                salir = False
        elif opcion == 9:
            salir = False
        else:
            print("Las notas todavía no están cargadas")
        limpiar_consola()
menu_competencia()