
# *Repositorio de la Materia Estructura de Datos*
---
# **Código "Arreglos"**

El código consiste en un registro de ventas mensuales por departamento de una tienda.  
Usa un **arreglo bidimensional (2D)** para almacenar los datos y permite:  
-Insertar ventas  
-Buscar ventas  
-Eliminar ventas  
-Mostrar las ventas en formato de tabla  

---

## **Métodos** 

### `mostrar_Tabla()`  
Muestra la tabla de ventas organizadas por mes y departamento usando la librería **tabulate**.  
- Crea una lista de listas donde cada fila representa un mes.  
- `tabulate()` organiza los datos en una tabla con formato `"grid"`.
- 
| Mes   | Departamento | Ventas |
|-------|-------------|--------|
| Enero | Ropa       | $500   |
| Febrero | Electrónica | $800   |

### `insertar_Venta()`  
Permite ingresar un valor de venta para un mes y departamento específico.  
- Pide al usuario el mes y departamento.  
- Solicita el valor de la venta y lo convierte en `float`.  
- Verifica si el mes y el departamento existen en las listas (`meses.index(mes)`, `departamentos.index(depto)`).  
- Si son correctos, almacena el valor en la matriz `"ventas"`.  
- Si hay un error, muestra un mensaje.  

### `buscar_Venta()`  
Permite buscar cuánto se vendió en un mes y departamento específico.  
- Solicita el mes y el departamento.  
- Verifica si están en las listas `"meses"

