#include <stdio.h>
#include <stdlib.h>

// ============================================================
// Estrutura que representa UM cartao dentro da fila do banco.
// Cada cartao guarda: o numero dele, se e comum ou prioritario,
// e um ponteiro apontando para o proximo cartao da fila.
// ============================================================
typedef struct Cartao {
    int numeroCartao;           // numero do cartao (ex: 1, 2, 301, 302...)
    char tipoPrioridade;        // 'C' = comum   |   'P' = prioritario
    struct Cartao *proximoCartao; // aponta para o proximo cartao da fila (ou NULL se for o ultimo)
} Cartao;

// Variavel global que guarda o PRIMEIRO cartao da fila (inicio da lista ligada)
Cartao *primeiroCartaoDaFila = NULL;

// Contadores usados para gerar o numero de cada cartao automaticamente
int proximoNumeroCartaoComum = 1;         // cartoes "C" comecam em 1
int proximoNumeroCartaoPrioritario = 301; // cartoes "P" comecam em 301


// ============================================================
// FUNCAO: inserirSemPrioridade
// Objetivo: colocar um cartao "C" (comum) no FINAL da fila.
// ============================================================
void inserirSemPrioridade(Cartao *cartaoParaInserir) {

    // Se a fila estiver vazia, o novo cartao vira o primeiro da fila
    if (primeiroCartaoDaFila == NULL) {
        primeiroCartaoDaFila = cartaoParaInserir;
        return;
    }

    // Ponteiro auxiliar que comeca no inicio da fila,
    // usado so para "andar" pela fila sem perder a referencia do inicio
    Cartao *cartaoQueEstouVisitando = primeiroCartaoDaFila;

    // Anda cartao por cartao ate encontrar o ULTIMO
    // (o ultimo e aquele cujo "proximoCartao" e NULL)
    while (cartaoQueEstouVisitando->proximoCartao != NULL) {
        cartaoQueEstouVisitando = cartaoQueEstouVisitando->proximoCartao;
    }

    // Encontrou o ultimo cartao da fila: conecta o novo cartao depois dele
    cartaoQueEstouVisitando->proximoCartao = cartaoParaInserir;
}


// ============================================================
// FUNCAO: inserirComPrioridade
// Objetivo: colocar um cartao "P" (prioritario) depois de TODOS
// os "P" que ja estao na fila, mas ANTES de qualquer cartao "C".
// ============================================================
void inserirComPrioridade(Cartao *cartaoParaInserir) {

    // Caso 1: a fila esta vazia OU o primeiro cartao ja e "C"
    // Nesses dois casos, o cartao novo vira o novo PRIMEIRO da fila
    if (primeiroCartaoDaFila == NULL || primeiroCartaoDaFila->tipoPrioridade == 'C') {
        cartaoParaInserir->proximoCartao = primeiroCartaoDaFila;
        primeiroCartaoDaFila = cartaoParaInserir;
        return;
    }

    // Ponteiro auxiliar para andar pela fila
    Cartao *cartaoQueEstouVisitando = primeiroCartaoDaFila;

    // Anda enquanto o PROXIMO cartao ainda for prioritario "P"
    // (ou seja, para assim que achar o fim do "bloco" de cartoes P)
    while (cartaoQueEstouVisitando->proximoCartao != NULL &&
           cartaoQueEstouVisitando->proximoCartao->tipoPrioridade == 'P') {
        cartaoQueEstouVisitando = cartaoQueEstouVisitando->proximoCartao;
    }

    // Encontrou o ultimo "P" da fila: encaixa o novo cartao logo depois dele
    cartaoParaInserir->proximoCartao = cartaoQueEstouVisitando->proximoCartao;
    cartaoQueEstouVisitando->proximoCartao = cartaoParaInserir;
}


// ============================================================
// FUNCAO: inserir
// Objetivo: perguntar ao usuario a prioridade, gerar o numero
// do cartao automaticamente e decidir qual funcao de insercao chamar.
// ============================================================
void inserir() {

    char prioridadeDigitadaPeloUsuario;

    printf("Digite a prioridade do cartao (C ou P): ");
    scanf(" %c", &prioridadeDigitadaPeloUsuario);

    // Aloca memoria para um novo cartao
    Cartao *cartaoNovo = malloc(sizeof(Cartao));

    // Guarda a prioridade escolhida pelo usuario dentro do cartao
    cartaoNovo->tipoPrioridade = prioridadeDigitadaPeloUsuario;

    // Por enquanto o cartao novo nao aponta para ninguem
    cartaoNovo->proximoCartao = NULL;

    // Define o numero do cartao de acordo com o tipo escolhido,
    // e depois AVANCA o contador correspondente para o proximo cliente
    if (prioridadeDigitadaPeloUsuario == 'C') {
        cartaoNovo->numeroCartao = proximoNumeroCartaoComum;
        proximoNumeroCartaoComum = proximoNumeroCartaoComum + 1;
    } else {
        cartaoNovo->numeroCartao = proximoNumeroCartaoPrioritario;
        proximoNumeroCartaoPrioritario = proximoNumeroCartaoPrioritario + 1;
    }

    // Decide onde o cartao novo deve entrar na fila
    if (primeiroCartaoDaFila == NULL) {
        // fila vazia: o cartao novo vira o primeiro
        primeiroCartaoDaFila = cartaoNovo;
    } else if (prioridadeDigitadaPeloUsuario == 'C') {
        // cartao comum: vai para o final da fila
        inserirSemPrioridade(cartaoNovo);
    } else {
        // cartao prioritario: entra depois dos outros "P"
        inserirComPrioridade(cartaoNovo);
    }
}


// ============================================================
// FUNCAO: imprimirFilaClientes
// Objetivo: mostrar na tela todos os cartoes da fila,
// do primeiro ate o ultimo.
// ============================================================
void imprimirFilaClientes() {

    Cartao *cartaoQueEstouVisitando = primeiroCartaoDaFila;

    // Percorre a fila inteira ate chegar no final (NULL)
    while (cartaoQueEstouVisitando != NULL) {
        printf("%c%d\n", cartaoQueEstouVisitando->tipoPrioridade,
                          cartaoQueEstouVisitando->numeroCartao);
        cartaoQueEstouVisitando = cartaoQueEstouVisitando->proximoCartao;
    }
}


// ============================================================
// FUNCAO: atenderCliente
// Objetivo: remover o primeiro cartao da fila (o proximo a ser
// atendido) e avisar na tela qual cliente foi chamado.
// ============================================================
void atenderCliente() {

    // Se a fila estiver vazia, nao ha ninguem para atender
    if (primeiroCartaoDaFila == NULL) {
        printf("Fila vazia.\n");
        return;
    }

    // Guarda o cartao que vai ser removido (o primeiro da fila)
    Cartao *cartaoQueSeraAtendido = primeiroCartaoDaFila;

    // A fila passa a comecar no SEGUNDO cartao
    primeiroCartaoDaFila = primeiroCartaoDaFila->proximoCartao;

    printf("Chamando cliente %c%d\n",
           cartaoQueSeraAtendido->tipoPrioridade,
           cartaoQueSeraAtendido->numeroCartao);

    // Libera a memoria do cartao que ja foi atendido
    free(cartaoQueSeraAtendido);
}


// ============================================================
// FUNCAO PRINCIPAL: main
// Objetivo: mostrar o menu de opcoes e chamar a funcao certa
// de acordo com a escolha do usuario, ate ele digitar 4 (sair).
// ============================================================
int main() {

    int opcaoEscolhidaPeloUsuario;

    do {
        printf("\n1-Adicionar cliente  2-Mostrar fila  3-Chamar cliente  4-Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcaoEscolhidaPeloUsuario);

        if (opcaoEscolhidaPeloUsuario == 1) {
            inserir();
        } else if (opcaoEscolhidaPeloUsuario == 2) {
            imprimirFilaClientes();
        } else if (opcaoEscolhidaPeloUsuario == 3) {
            atenderCliente();
        }
        // se digitar 4, o loop simplesmente vai parar la embaixo
        // se digitar outra coisa, o menu aparece de novo

    } while (opcaoEscolhidaPeloUsuario != 4);

    return 0;
}