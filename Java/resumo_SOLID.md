# Princípios SOLID

Os princípios SOLID ajudam a escrever código mais limpo, organizado, reutilizável e fácil de manter. Eles são muito usados na Programação Orientada a Objetos.

## S — Single Responsibility Principle (Princípio da Responsabilidade Única)

> Uma classe deve ter apenas uma razão para mudar.

- Cada classe deve fazer **uma coisa só** (ex: ou ela calcula, ou ela envia emails, mas não os dois).
- Isso deixa o código **mais fácil de entender** e de manter.
- Quando algo muda no sistema, **somente a classe responsável** por essa tarefa deve ser alterada.
- Ajuda a **evitar bugs**, porque mudanças em uma parte não afetam outras inesperadamente.
- Facilita **testes unitários**, porque cada classe tem uma função bem definida.

## O — Open/Closed Principle (Princípio Aberto/Fechado)

> Entidades devem estar **abertas para extensão**, mas **fechadas para modificação**.

- Você pode **adicionar novas funcionalidades** sem mudar o código original.
- Ajuda a **não quebrar** funcionalidades já existentes.
- Usamos herança ou interfaces para **extender comportamentos**.
- Garante que o sistema seja **mais flexível e escalável**.
- Reduz o risco de **introduzir erros** ao modificar código já testado.

## L — Liskov Substitution Principle (Princípio da Substituição de Liskov)

> Subtipos devem poder substituir seus tipos base **sem alterar o comportamento do sistema**.

- Se uma classe `Filha` herda de uma classe `Pai`, ela deve funcionar como substituta sem problemas.
- O código que usa a classe pai **não deve precisar saber** se está lidando com uma filha.
- Garante **consistência no uso da herança**.
- Evita que **funções que usam polimorfismo se comportem de forma inesperada**.
- Ajuda a manter **contratos e regras esperadas** do sistema.

## I — Interface Segregation Principle (Princípio da Segregação de Interfaces)

> Uma classe **não deve ser forçada a implementar métodos que não usa**.

- Prefira criar **interfaces pequenas e específicas** em vez de uma grande com métodos desnecessários.
- Ajuda a **evitar código inútil** ou "implementações vazias".
- Melhora a **clareza do que cada classe precisa fazer**.
- Permite que **módulos sejam mais independentes**.
- Garante que **cada classe dependa só do que realmente precisa**.

## D — Dependency Inversion Principle (Princípio da Inversão de Dependência)

> Dependa de **abstrações**, e não de implementações concretas.

- Em vez de usar diretamente uma classe (`new Classe()`), use **interfaces ou abstrações**.
- Torna o código **mais flexível** e fácil de mudar.
- Facilita a **injeção de dependência** (como usar um serviço de email falso em testes).
- Ajuda a **desacoplar as partes do sistema**.
- É um dos princípios base do conceito de **arquitetura limpa**.

------------------------------------------------

Os princípios **SOLID** ajudam a escrever um código:

- Mais limpo.
- Mais fácil de manter.
- Mais organizado.
- Escalável
- Com menos bugs.
