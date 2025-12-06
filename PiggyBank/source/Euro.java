package source;

public class Euro extends Moeda {
    private static final double TAXA_CAMBIO = 6.2;

    public Euro(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return valor * TAXA_CAMBIO;
    }

    @Override
    public String getNome() {
        return "Euro";
    }
}