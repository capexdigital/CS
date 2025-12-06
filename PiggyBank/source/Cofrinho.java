package source;

import java.util.ArrayList;
import java.util.List;

public class Cofrinho {
    private List<Moeda> moedas;

    public Cofrinho() {
        moedas = new ArrayList<>();
    }

    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);
        System.out.println("Moeda adicionada com sucesso!");
    }

    public boolean removerMoeda(int indice) {
        if (indice >= 0 && indice < moedas.size()) {
            moedas.remove(indice);
            return true;
        }
        return false;
    }

    public void listarMoedas() {
        if (moedas.isEmpty()) {
            System.out.println("Cofrinho vazio!");
            return;
        }

        for (int i = 0; i < moedas.size(); i++) {
            Moeda m = moedas.get(i);
            System.out.printf("%d. %s (R$ %.2f)\n", i+1, m, m.converterParaReal());
        }
    }

    public double calcularTotalEmReal() {
        double total = 0;
        for (Moeda m : moedas) {
            total += m.converterParaReal();
        }
        return total;
    }

    public List<Moeda> getMoedas() {
        return moedas;
    }
}