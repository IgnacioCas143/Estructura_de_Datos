calificaciones = [0] * 5  

for i in range(5):
    calificaciones[i] = int(input(f"Captura la calificación {i + 1}: "))

print("Calificaciones:", calificaciones)

frutas = ["Mango", "Manzana", "Banana", "Uvas"]
print(frutas)

frutas.pop(0)  
frutas.pop(1)  

frutas.append("Sandía")
print(frutas)
