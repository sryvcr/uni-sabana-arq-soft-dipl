class OrdenPostre extends Orden {
    @Override
    protected boolean estaDisponible() {
        System.out.println("Verificando disponibilidad del postre...");
        return false; 
    }

    @Override
    protected void calcularPrecio() {
        System.out.println("Calculando precio del postre: $8.00");
    }
}
