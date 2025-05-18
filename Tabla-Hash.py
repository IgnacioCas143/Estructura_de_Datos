
datos = [
    "Grupo Solar,2,2023-06-10|2023-06-24",
    "Ensamble Luna,1,2023-07-15",
    "Dúo Estrella,3,2023-08-05|2023-08-12|2023-08-19"
]

presentaciones = {}
for linea in datos:
    partes = linea.strip().split(",")
    nombre = partes[0]
    fechas = partes[2].split("|")
    presentaciones[nombre] = fechas

grupo = input("Ingresa el nombre del grupo: ").strip().lower()
presentaciones_normalized = {k.lower(): v for k, v in presentaciones.items()}
if grupo in presentaciones_normalized:
    print(f"Fechas de presentación de {grupo}: {presentaciones_normalized[grupo]}")
else:
    print("Grupo no encontrado.")
    
print("-"*70)
    
usuarios = {
    "jsmith": "jsmith@email.com",
    "mlopez": "mlopez@email.com",
    "arivera": "arivera@email.com",
    "cgarcia": "cgarcia@email.com"
}

usuario = input("Ingresa el nombre de usuario: ").strip().lower()

if usuario in usuarios:
    print(f"El correo electrónico de {usuario} es: {usuarios[usuario]}")
else:
    print("Usuario no encontrado.")
