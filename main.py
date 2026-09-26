# Sistema Inteligente Basado en Reglas - Transporte Masivo
# Estilo: diccionario (base de conocimiento), (regla de busqueda)
 
# --------------------------------------------------------------
# BASE DE CONOCIMIENTO: cada estacion apunta a la lista de
# estaciones con las que tiene conexion directa.
# --------------------------------------------------------------
rutas = {
    "Portal Sur": ["Perdomo", "Madelena"],
    "Perdomo": ["Portal Sur", "Madelena"],
    "Madelena": ["Portal Sur", "Perdomo", "Alqueria"],
    "Alqueria": ["Madelena", "Banderas"],
    "Banderas": ["Alqueria", "Ricaurte", "Avenida El Dorado"],
    "Ricaurte": ["Banderas", "Centro Memoria", "Portal El Dorado"],
    "Centro Memoria": ["Ricaurte", "Portal El Dorado"],
    "Avenida El Dorado": ["Banderas", "Portal El Dorado"],
    "Portal El Dorado": ["Ricaurte", "Centro Memoria", "Avenida El Dorado"]
}
 
 
# --------------------------------------------------------------
# REGLA PARA BUSCAR UNA RUTA Funcion Recursiva
# --------------------------------------------------------------
def buscar_ruta(origen, destino, ruta=[]):
 
    ruta = ruta + [origen]
 
    # Si llegamos al destino
    if origen == destino:
        return ruta
 
    # Si la estacion no existe en la base de conocimiento
    if origen not in rutas:
        return None 
    # Revisar las estaciones conectadas
    for vecino in rutas[origen]:
        if vecino not in ruta:  # evitar dar vueltas en circulo
            resultado = buscar_ruta(vecino, destino, ruta)
            if resultado is not None:
                return resultado
 
    # Si ningun vecino lleva al destino
    return None
 
 
# --------------------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------------------
print("Estaciones disponibles:", ", ".join(rutas.keys()))
print("\nIngrese la estacion de origen exactamente como se muestran en la lista tanto mayusculas como minusculas")
origen = input("Estacion de ORIGEN: ").strip()
print("\nIngrese la estacion de destino exactamente como se muestran en la lista tanto mayusculas como minusculas.")
destino = input("Estacion de DESTINO: ").strip()
 
if origen not in rutas or destino not in rutas:
    print("\nUna de las estaciones no existe en la base de conocimiento o fue escrita incorrectamente.")
else:
    camino = buscar_ruta(origen, destino)
    if camino:
        print("\nRuta encontrada:")
        print(" -> ".join(camino))
        print(f"Numero de estaciones recorridas (sin contar la de origen): {len(camino)-1}")
    else:
        print("\nNo se encontro una ruta entre esas estaciones.")