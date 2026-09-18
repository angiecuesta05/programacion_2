yo = {"nombre": "Angie", "edad": 20, "es_estudiante": True}

yo_lista = ["Angie", 18, True]
print(yo_lista[0])
print(yo["nombre"])

# Modificar un elemento
yo_lista[0] = "Angie Cuesta"
print(yo_lista)
yo["nombre"] = "Angie Cuesta"
print(yo)

# Agregar un elemento
yo_lista.append("Barranquilla")  # -->Lista
yo["direccion"] = "Barranquilla"
yo["telefono"] = "3005092510"

# update
yo_2 = {"rh": "o-", "profesion": "Estadistico"}
yo.update(yo_2)
print(yo)

# eliminar elementos
eliminado_1 = yo.pop("profesion")
eliminado_2 = yo.pop("rh")
print(eliminado_1)
print()
