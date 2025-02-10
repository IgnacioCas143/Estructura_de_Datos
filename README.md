# Estructura_de_Datos
Repositorio de la Materia Estructura de Datos
📌 mostrarTabla()
Muestra la tabla de ventas organizadas por mes y departamento usando la librería tabulate.
🔹 Crea una lista de listas donde cada fila representa un mes.
🔹 tabulate() organiza los datos en una tabla con formato "grid".

📌 insertarVenta()
Permite ingresar un valor de venta para un mes y departamento específico.
🔹 Pide al usuario el mes y departamento.
🔹 Solicita el valor de la venta y lo convierte en float.
🔹 Verifica si el mes y el departamento existen en las listas (meses.index(mes), departamentos.index(depto)).
🔹 Si son correctos, almacena el valor en la matriz "ventas".
🔹 Si hay un error, muestra un mensaje.

📌 buscarVenta()
Permite buscar cuánto se vendió en un mes y departamento específico.
🔹 Solicita el mes y el departamento.
🔹 Verifica si están en las listas "meses", "departamentos".
🔹 Muestra el valor almacenado en la matriz "ventas".
🔹 Si hay un error, muestra un mensaje.

📌 eliminarVenta()
Permite eliminar una venta estableciendo su valor en 0.
🔹 Solicita el mes y el departamento.
🔹 Verifica si están en las listas "meses", "departamentos".
🔹 Restablece el valor en 0 en la matriz "ventas".
🔹 Muestra "Venta en {Mes}-{Departamento} eliminada" o un mensaje de error si no existe.
