package source;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();
        int opcao;

        do {
            System.out.println("\n=== COFRINHO DE MOEDAS ===");
            System.out.println("1. Adicionar moeda");
            System.out.println("2. Remover moeda");
            System.out.println("3. Listar moedas");
            System.out.println("4. Calcular total em Real");
            System.out.println("0. Sair");
            System.out.print("Opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    adicionarMoeda(scanner, cofrinho);
                    break;
                case 2:
                    removerMoeda(scanner, cofrinho);
                    break;
                case 3:
                    cofrinho.listarMoedas();
                    break;
                case 4:
                    System.out.printf("Total: R$ %.2f\n", cofrinho.calcularTotalEmReal());
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }

            if (opcao != 0) {
                System.out.println("\nPressione Enter...");
                scanner.nextLine();
                scanner.nextLine();
            }
        } while (opcao != 0);

        scanner.close();
    }

    private static void adicionarMoeda(Scanner scanner, Cofrinho cofrinho) {
        System.out.println("\nTipo: 1-Real 2-Dólar 3-Euro");
        System.out.print("Escolha: ");
        int tipo = scanner.nextInt();

        System.out.print("Valor: ");
        double valor = scanner.nextDouble();

        Moeda moeda;
        if (tipo == 1) {
            moeda = new Real(valor);
        } else if (tipo == 2) {
            moeda = new Dolar(valor);
        } else if (tipo == 3) {
            moeda = new Euro(valor);
        } else {
            System.out.println("Tipo inválido!");
            return;
        }

        cofrinho.adicionarMoeda(moeda);
    }

    private static void removerMoeda(Scanner scanner, Cofrinho cofrinho) {
        if (cofrinho.getMoedas().isEmpty()) {
            System.out.println("Cofrinho vazio!");
            return;
        }

        cofrinho.listarMoedas();
        System.out.print("Número da moeda a remover: ");
        int indice = scanner.nextInt() - 1;

        if (cofrinho.removerMoeda(indice)) {
            System.out.println("Moeda removida!");
        } else {
            System.out.println("Erro ao remover!");
        }
    }
}