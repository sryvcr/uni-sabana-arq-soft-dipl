class OrdenComida extends Orden {
    @Override
    protected boolean estaDisponible() {
        System.out.println("Verificando disponibilidad de comida...");
        return true; 
    }

    @Override
    protected void calcularPrecio() {
        System.out.println("Calculando precio de la comida: $15.00");
    }
}
