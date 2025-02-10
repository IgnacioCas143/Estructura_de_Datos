# Estructura_de_Datos
Repositorio de la Materia Estructura de Datos
Código "Arreglos" PYTHON
El código consiste en un registro de ventas mensuales por departamento de una dienta, usa un arreglo bidimiensional(2D) para almacenar los datos, permite insetar, buscar y eliminar las ventas, además de mostar las ventas en formato de tabla.
Método "Mostrar Tabla"
Muestra la tabla de ventas organizadas por mes y departamento usando la librería (tabulate), que le da un formato de tabla estructurada. Crea una lista de listas donde cada fila representa un mes y tabulate() organioza los datos en una tabla con formato "grid"
Método "Insertar venta"
Permite ingresar un valor de venta para un mes y despartamento específico. Pide al usuario el mes y departamento,pie del valor de la venta y lo convierte en float, luego verifica si el mes y el departamento existen en las listas (meses.index(mes) y departamentos.index(depto) , si son correctos, almacena el valor en la matriz "ventas", sino muestra "error".
Método "Buscar venta"
Permite buscar cúanto se vendió en un mes y departamento específico. Solicita el mes y departamento, verifica si estan en las listas "meses","departamentos" y muestra el valor almacenado en la matriz "ventas", sino muestra "error".
Método "Eliminar venta"
Deja eliminar una venta estableciendo su valor en 0. Solicita el mes y departamento, verifica si estan en las listas "meses","departamentos"; reestablece el valor en "0" almacenado en la matriz "ventas" y muestra "" Venta en {Mes}-{Departmento} eliminada"" , sino muestra "error".
