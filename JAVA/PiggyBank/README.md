**ATIVIDADE PRÁTICA**

Cofrinho de Moedas – Projeto Java

Descrição
O projeto consiste em criar um sistema em Java que simula um cofrinho de moedas.
O foco é demonstrar o uso correto de herança, polimorfismo e coleções.

Objetivos

* Adicionar moedas de diferentes países e valores no cofrinho
* Remover moedas específicas
* Listar todas as moedas presentes
* Calcular o valor total convertido para Real (BRL)

Estrutura do Projeto

* Classe Principal: responsável pelo menu e interação com o usuário
* Classe Cofrinho: armazena uma coleção de objetos do tipo Moeda (ex: ArrayList)
* Classe abstrata Moeda: classe mãe comum para as moedas
* Classes filhas: Dolar, Euro, Real (ou outras), cada uma implementando seus próprios métodos de conversão e exibição

Requisitos Técnicos

* Uso obrigatório de herança e polimorfismo
* Utilização de coleções (preferencialmente ArrayList)
* Possibilidade de adicionar, remover, listar e converter moedas
* Liberdade para criar métodos adicionais se necessário

Funcionamento Esperado

1. O programa exibe um menu
2. O usuário pode adicionar moedas
3. O usuário pode remover moedas
4. O programa lista todas as moedas do cofrinho
5. O programa mostra o total em Reais

---

* Herança (Real/Dolar/Euro extendem Moeda)

* Polimorfismo (List<Moeda> pode ter qualquer subtipo)

* Classes abstratas (Moeda é abstract)

* Coleções (ArrayList<Moeda>)

**TUTORIAL**

WINDOWS
1. Extrair ZIP
   
   
    C:\Users\Exemplo\Documents\PiggyBank


2. Entrar na pasta source rodando o comando no powershell
   

    cd C:\PiggyBank\source


3. Compilar o projeto

   
    javac *.java

   * Se aparecer erro "javac não é reconhecido", instale o Java:


4. Rodar


    java Main

   
LINUX

1. Extrair zip usando bash


    unzip PiggyBank.zip

   * se estiver em /Downloads
   

     cd ~/Downloads
     unzip PiggyBank.zip -d ~/PiggyBank

isso criará 

    ~/PiggyBank/source/*.java

2. acessar a pasta do código fonte

    
    cd ~/PiggyBank/source

3. Compilar


    javac source/*.java


4. Rodar


    java source.Main



    



