import statistics
import random
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def sueldos_aleatorio():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos aleatorios asignados.")


def clas_sueldo():
    print("\nListado de trabajadores y sus sueldos:")
    for i, trabajador in enumerate(trabajadores):
        print(f"{trabajador}: ${sueldos[i]}")


def  estadisticas():
    if not sueldos:
        print("Primero tienes que asignar sueldos aleatorios.")
        return
    
    print("\nEstadísticas de sueldos:")
    print(f"Sueldo más alto: ${max(sueldos)}")
    print(f"Sueldo más bajo: ${min(sueldos)}")
    print(f"Promedio de sueldos: ${statistics.mean(sueldos)}")
    
    
    prod = 1
    for sueldo in sueldos:
        prod *= sueldo
    media_geom = math.pow(prod, 1 / len(sueldos))
    print(f"Media Geométrica: ${media_geom:.2f}")


def    reporte():
    if not sueldos:
        print("Primero debes asignar sueldos aleatorios.")
        return
    
    print("""\nReporte de sueldos: 
          *************************************************************""")
for i, empleado in enumerate(trabajadores):
        sueldo = sueldos[i]
        salud = sueldo * 0.07
        afp = sueldo * 0.12
        sueldo_liquido = sueldo - salud - afp
        print("""__________________________________________________________
                  |Empleado      |    Sueldo    |   Sueldo Líquido|""")
        print("************************************************************")  
        print(f"| {empleado:17} | ${sueldo:8} | ${sueldo_liquido:13.2f} |")
        print("********************************************************")


def main():
    while True:
        print("\nMenú:")
        print ("""
        1. Asignar sueldos aleatorios")
        2. Clasificar sueldos
        3. Ver estadísticas     
        4. Reporte de sueldos
        5. Salir del programa
        """)
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == "1":
              sueldos_aleatorio()
        elif opcion == "2":
                clas_sueldo()
        elif opcion == "3":
             estadisticas()
        elif opcion == "4":
                reporte()
        elif opcion == "5":
            print("¡Programa finalizado!")
            print("""
                  Tomas Rodriguez
                  21.375.517-k
                  """)
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
