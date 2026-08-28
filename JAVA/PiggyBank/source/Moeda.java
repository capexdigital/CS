package source;

// Classe abstrata que será herdada por todas as moedas
public abstract class Moeda {
    protected double valor;

    // Construtor
    public Moeda(double valor) {
        this.valor = valor;
    }

    // Método abstrato para converter para Real
    public abstract double converterParaReal();

    // Método abstrato para obter nome da moeda
    public abstract String getNome();

    // Getter para valor
    public double getValor() {
        return valor;
    }

    // Método para exibir informações
    @Override
    public String toString() {
        return String.format("%s: %.2f", getNome(), valor);
    }
}