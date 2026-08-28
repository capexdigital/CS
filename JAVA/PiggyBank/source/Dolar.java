package source;

public class Dolar extends Moeda {
    private static final double TAXA = 5.4;

    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return valor * TAXA;
    }

    @Override
    public String getNome() {
        return "Dólar";
    }
}