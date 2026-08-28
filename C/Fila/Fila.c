#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Estrutura base do cartão
typedef struct Cartao {
    int numeroCartao;
    char tipoPrioridade;
    struct Cartao *proximoCartao;
} Cartao;
    
Cartao *primeiroCartaoDaFila = NULL;

int proximoNumeroCartaoComum = 1;
int proximoNumeroCartaoPrioritario = 301;

void inserirSemPrioridade(Cartao *cartaoParaInserir) {
    Cartao **ponteiroDeInsercao = &primeiroCartaoDaFila;
    while (*ponteiroDeInsercao != NULL)
        ponteiroDeInsercao = &(*ponteiroDeInsercao)->proximoCartao;
    *ponteiroDeInsercao = cartaoParaInserir;
}

void inserirComPrioridade(Cartao *cartaoParaInserir) {
    Cartao **ponteiroDeInsercao = &primeiroCartaoDaFila;
    while (*ponteiroDeInsercao != NULL && (*ponteiroDeInsercao)->tipoPrioridade == 'P')
        ponteiroDeInsercao = &(*ponteiroDeInsercao)->proximoCartao;
    cartaoParaInserir->proximoCartao = *ponteiroDeInsercao;
    *ponteiroDeInsercao = cartaoParaInserir;
}

void inserir() {
    char prioridadeDigitadaPeloUsuario;

    // Utiliza toupper para transformar inputs em letra maiúscula
    do {
        printf("Prioridade (C ou P): ");
        scanf(" %c", &prioridadeDigitadaPeloUsuario);
        prioridadeDigitadaPeloUsuario = toupper(prioridadeDigitadaPeloUsuario);

        // Aceita apenas "C" ou "P"
        if (prioridadeDigitadaPeloUsuario != 'C' && prioridadeDigitadaPeloUsuario != 'P')
            printf("Erro: digite apenas C ou P.\n");

    } while (prioridadeDigitadaPeloUsuario != 'C' && prioridadeDigitadaPeloUsuario != 'P');

    Cartao *cartaoNovo = malloc(sizeof(Cartao));
    cartaoNovo->tipoPrioridade = prioridadeDigitadaPeloUsuario;
    cartaoNovo->proximoCartao = NULL;
    cartaoNovo->numeroCartao = (prioridadeDigitadaPeloUsuario == 'C')
        ? proximoNumeroCartaoComum++ : proximoNumeroCartaoPrioritario++;

    if (prioridadeDigitadaPeloUsuario == 'C')
        inserirSemPrioridade(cartaoNovo);
    else
        inserirComPrioridade(cartaoNovo);
}

// Função que percorre toda a lista, e retorna a fila atual de clientes
void imprimirFilaClientes() {
    for (Cartao *cartaoAtual = primeiroCartaoDaFila; cartaoAtual != NULL; cartaoAtual = cartaoAtual->proximoCartao)
        printf("%c%d\n", cartaoAtual->tipoPrioridade, cartaoAtual->numeroCartao);
}

// Função para chamar próximo cliente da fila
void atenderCliente() {
    if (primeiroCartaoDaFila == NULL) { printf("Fila vazia.\n"); return; }
    Cartao *cartaoQueSeraAtendido = primeiroCartaoDaFila;
    primeiroCartaoDaFila = primeiroCartaoDaFila->proximoCartao;
    printf("Chamando cliente %c%d\n", cartaoQueSeraAtendido->tipoPrioridade, cartaoQueSeraAtendido->numeroCartao);
    free(cartaoQueSeraAtendido);
}

// Menu principal
int main() {
    int opcaoEscolhidaPeloUsuario;
    do {
        printf("\n1-Nova Senha \n2-Mostrar Fila \n3-Chamar Proxima Senha \n4-Sair \nOpcao: ");
        scanf("%d", &opcaoEscolhidaPeloUsuario);
        if (opcaoEscolhidaPeloUsuario == 1) inserir();
        else if (opcaoEscolhidaPeloUsuario == 2) imprimirFilaClientes();
        else if (opcaoEscolhidaPeloUsuario == 3) atenderCliente();
    } while (opcaoEscolhidaPeloUsuario != 4);
    return 0;
}