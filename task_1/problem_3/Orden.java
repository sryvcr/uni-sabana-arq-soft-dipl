abstract class Orden {
    public final void procesarOrden() {
        tomarOrden();
        prepararOrden();
        if (estaDisponible()) {
            calcularPrecio();
            entregarOrden();
        } else {
            System.out.println("La orden no está disponible.");
        }
    }

    private void tomarOrden() {
        System.out.println("Tomando la orden...");
    }

    private void prepararOrden() {
        System.out.println("Preparando la orden...");
    }

    private void entregarOrden() {
        System.out.println("Entregando la orden...");
    }

    protected abstract boolean estaDisponible();
    protected abstract void calcularPrecio();
}
