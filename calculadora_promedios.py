"""
Calculadora de Promedios Escolares
Programa estructurado en Python para gestionar materias y calificaciones.
"""

def ingresar_calificaciones():
    """
    Solicita al usuario el nombre de la materia y su calificación.
    Valida que la calificación sea un float entre 0.0 y 10.0.
    Retorna dos listas: (materias, calificaciones).
    """
    materias = []
    calificaciones = []
    
    print("\n--- Registro de Calificaciones ---")
    while True:
        materia = input("Ingrese el nombre de la materia (o presione Enter para terminar): ").strip()
        if not materia:
            # Si no se ingresa materia, se pregunta si se quiere finalizar
            confirmar = input("¿Desea finalizar el ingreso de materias? (s/n, por defecto 's'): ").strip().lower()
            if confirmar in ('s', 'si', 'y', 'yes', ''):
                break
            else:
                continue
        
        # Validar calificación
        while True:
            try:
                calif_str = input(f"Ingrese la calificación de '{materia}' (0.0 a 10.0): ").strip()
                calificacion = float(calif_str)
                if 0.0 <= calificacion <= 10.0:
                    break
                else:
                    print("Error: La calificación debe ser un valor entre 0.0 y 10.0. Inténtelo de nuevo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido (ej. 8.5). Inténtelo de nuevo.")
        
        materias.append(materia)
        calificaciones.append(calificacion)
        
        # Preguntar si desea continuar
        opcion = input("¿Desea agregar otra materia? (s/n, por defecto 's'): ").strip().lower()
        if opcion in ('n', 'no'):
            break
            
    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Recibe una lista de calificaciones y devuelve su promedio aritmético.
    Si la lista está vacía, devuelve 0.0.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina qué materias están aprobadas y cuáles reprobadas según el umbral.
    Devuelve dos listas con los índices correspondientes.
    """
    aprobadas = []
    reprobadas = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
            
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Identifica el índice de la calificación más alta y el de la más baja.
    Si la lista está vacía, retorna (-1, -1).
    """
    if not calificaciones:
        return -1, -1
        
    val_max = calificaciones[0]
    val_min = calificaciones[0]
    idx_max = 0
    idx_min = 0
    
    for i, calif in enumerate(calificaciones):
        if calif > val_max:
            val_max = calif
            idx_max = i
        if calif < val_min:
            val_min = calif
            idx_min = i
            
    return idx_max, idx_min


def main():
    """
    Función principal que coordina la calculadora de promedios.
    """
    print("=============================================")
    print("   BIENVENIDO A LA CALCULADORA DE PROMEDIOS  ")
    print("=============================================")
    
    # Obtener datos del usuario
    materias, calificaciones = ingresar_calificaciones()
    
    # Manejo del caso especial: no se ingresó ninguna materia
    if not materias:
        print("\n[!] No se ingresó ninguna materia ni calificación.")
        print("No hay datos para calcular o mostrar.")
        print("\n=============================================")
        print("¡Gracias por utilizar la calculadora! Adiós. ")
        print("=============================================")
        return
        
    # Realizar cálculos
    promedio = calcular_promedio(calificaciones)
    aprobadas_idx, reprobadas_idx = determinar_estado(calificaciones)
    idx_max, idx_min = encontrar_extremos(calificaciones)
    
    # Mostrar resumen final
    print("\n=============================================")
    print("               RESUMEN FINAL                 ")
    print("=============================================")
    
    print("\n--- Lista de Materias y Calificaciones ---")
    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]:.2f}")
        
    print(f"\nPromedio General: {promedio:.2f}")
    
    print("\n--- Estado de las Materias ---")
    print("Aprobadas:")
    if aprobadas_idx:
        for idx in aprobadas_idx:
            print(f"  * {materias[idx]} ({calificaciones[idx]:.2f})")
    else:
        print("  (Ninguna materia aprobada)")
        
    print("Reprobadas:")
    if reprobadas_idx:
        for idx in reprobadas_idx:
            print(f"  * {materias[idx]} ({calificaciones[idx]:.2f})")
    else:
        print("  (Ninguna materia reprobada)")
        
    # Extremos (materia con mejor y peor calificación)
    if idx_max != -1 and idx_min != -1:
        print("\n--- Calificaciones Extremas ---")
        print(f"Materia con mejor calificación: {materias[idx_max]} ({calificaciones[idx_max]:.2f})")
        print(f"Materia con peor calificación: {materias[idx_min]} ({calificaciones[idx_min]:.2f})")
        
    print("\n=============================================")
    print("¡Gracias por utilizar la calculadora! Adiós. ")
    print("=============================================")


if __name__ == "__main__":
    main()
