import java.util.ArrayList;
import java.util.Scanner;

public class ListasArray {
    static Scanner scanner = new Scanner(System.in);
    static ArrayList<String> meses = new ArrayList<>();
    static ArrayList<String> departamentos = new ArrayList<>();
    static ArrayList<ArrayList<Double>> ventas = new ArrayList<>();

    public static void main(String[] args) {
        // Poner los meses
        String[] nombresMeses = {"enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                                 "septiembre", "octubre", "noviembre", "diciembre"};
        for (String mes : nombresMeses) {
            meses.add(mes);
            ventas.add(new ArrayList<>());
            for (int i = 0; i < 3; i++) {
                ventas.get(meses.indexOf(mes)).add(0.0);  // Inicializa con ceros
            }
        }

        // Poner los departamentos
        String[] nombresDepartamentos = {"ropa", "deportes", "juguetería"};
        for (String depto : nombresDepartamentos) {
            departamentos.add(depto);
        }

        int opcion;
        do {
            System.out.println("\n--- Menú de Ventas ---");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar tabla");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();  // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    insertarVenta();
                    break;
                case 2:
                    buscarVenta();
                    break;
                case 3:
                    eliminarVenta();
                    break;
                case 4:
                    mostrarTabla();
                    break;
                case 5:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida, intente de nuevo.");
            }
        } while (opcion != 5);
    }

    // Método para insertar una venta
    public static void insertarVenta() {
        System.out.print("Ingrese el mes: ");
        String mes = scanner.nextLine().trim().toLowerCase();
        System.out.print("Ingrese el departamento: ");
        String depto = scanner.nextLine().trim().toLowerCase();

        if (meses.contains(mes) && departamentos.contains(depto)) {
            System.out.print("Ingrese el valor de la venta: ");
            double valor = scanner.nextDouble();
            scanner.nextLine();  // Consumir el salto de línea

            int mesIndex = meses.indexOf(mes);
            int deptoIndex = departamentos.indexOf(depto);
            ventas.get(mesIndex).set(deptoIndex, valor);
            System.out.println("Venta registrada correctamente.");
        } else {
            System.out.println("Error: Mes o departamento inválido.");
        }
    }

    // Método para buscar una venta
    public static void buscarVenta() {
        System.out.print("Ingrese el mes a buscar: ");
        String mes = scanner.nextLine().trim().toLowerCase();
        System.out.print("Ingrese el departamento a buscar: ");
        String depto = scanner.nextLine().trim().toLowerCase();

        if (meses.contains(mes) && departamentos.contains(depto)) {
            int mesIndex = meses.indexOf(mes);
            int deptoIndex = departamentos.indexOf(depto);
            System.out.println("La venta en " + mes + " - " + depto + " es: " + ventas.get(mesIndex).get(deptoIndex));
        } else {
            System.out.println("Error: Mes o departamento inválido.");
        }
    }

    // Método para eliminar una venta
    public static void eliminarVenta() {
        System.out.print("Ingrese el mes a eliminar: ");
        String mes = scanner.nextLine().trim().toLowerCase();
        System.out.print("Ingrese el departamento a eliminar: ");
        String depto = scanner.nextLine().trim().toLowerCase();

        if (meses.contains(mes) && departamentos.contains(depto)) {
            int mesIndex = meses.indexOf(mes);
            int deptoIndex = departamentos.indexOf(depto);
            ventas.get(mesIndex).set(deptoIndex, 0.0);
            System.out.println("Venta eliminada correctamente.");
        } else {
            System.out.println("Error: Mes o departamento inválido.");
        }
    }

    // Método para mostrar la tabla
    public static void mostrarTabla() {
        System.out.println("\n--- Tabla de Ventas ---");
        System.out.printf("%-12s %-12s %-12s %-12s%n", "Mes", "Ropa", "Deportes", "Juguetería");
        System.out.println("-------------------------------------------------");

        for (int i = 0; i < meses.size(); i++) {
            System.out.printf("%-12s %-12.2f %-12.2f %-12.2f%n",
                              meses.get(i),
                              ventas.get(i).get(0),
                              ventas.get(i).get(1),
                              ventas.get(i).get(2));
        }
    }
}
