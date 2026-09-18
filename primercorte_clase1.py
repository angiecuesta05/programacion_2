nombres = []
telefonos = []
emails = []
direcciones = []

contactos = {}

while True:
    menu = """

    ### ELIGE UNA OPCION ###

    1. Agregar un contacto
    2. Busca un contacto
    3. Eliminar un contacto
    4. Ver contactos
    5. Salir
    """

    opcion elegida = int(input(menu))

if opcion_elegida == 1:
    nombre = input("Ingrese el nombre:")
    nombre = nombre_lower()
    telefono = input("Ingrese el telefono:")
    email = input("Ingrese su email:")
    direccion = input("Ingrese su direccion:")
    contactos[nombre]={
        "telefono": telefono,
        "email": email,
        "direccion": direccion
    }
    print(f"Contacto{contactos} guardado exitosamente ✅")
elif opcion_elegida == 2:
    nombre = input("Ingrese el nombre a buscar:").lower()
    if nombre in contactos:
        print("="*10)
        print(contactos[nombre])
        print("="*10)

    else:
        print("Contacto no existe")
elif opcion_elegida == 3:
    nombre = input("Ingrese el nombre del contacto a eliminar:").lower()
    if nombre in nombres:
        indice = nombres.index(nombre.lower())
        nombres.pop(indice)
        telefonos.pop(indice)
        emails.pop(indice)
        direcciones.pop(indice)
    pass
elif opcion_elegida == 4:
    for nombre, telefono, email, direccion in zip(nombres, telefonos, emails, direcciones):
    print(f"Nombre: {nombre}")
    print(f"Telefono: {telefono}")
    print(f"Email:{email}")
    print(f"Direccion: {direccion}")
    print("Hasta la vista baby")
    break
else:
    print("opcion invalida intenta nuevamente")

          
