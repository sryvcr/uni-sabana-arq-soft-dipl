public class Principal {
    public static void main(String[] args) {
        Orden ordenComida = new OrdenComida();
        Orden ordenBebida = new OrdenBebida();
        Orden ordenPostre = new OrdenPostre();

        System.out.println("Procesando orden de comida:");
        ordenComida.procesarOrden();
        System.out.println("\nProcesando orden de bebida:");
        ordenBebida.procesarOrden();
        System.out.println("\nProcesando orden de postre:");
        ordenPostre.procesarOrden();
    }
}
