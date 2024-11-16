class OrdenBebida extends Orden {
    @Override
    protected boolean estaDisponible() {
        System.out.println("Verificando disponibilidad de la bebida...");
        return true;
    }

    @Override
    protected void calcularPrecio() {
        System.out.println("Calculando precio de la bebida: $5.00");
    }
}
