# Aula 3 - Introdução à Computação

## 1. Informação vs Dados

### Era do Conhecimento e Informação
- **Conceito:** Peter Drucker (1966) definiu nossa época como "sociedade da informação"
- **Características atuais:**
  - Profusão excessiva de informações válidas e inválidas
  - Acesso rápido (milésimos de segundo) a qualquer informação
  - Dependência tecnológica para acesso aos dados
  - Qualidade e veracidade desconhecidas das informações disponíveis

### Hierarquia: Dados → Informação → Conhecimento

| **Dados** | **Informação** | **Conhecimento** |
|-----------|----------------|------------------|
| Simples observações sobre o estado do mundo | Dados dotados de relevância e propósito | Informação valiosa da mente humana com reflexão, síntese e contexto |
| Facilmente estruturado e obtido por máquinas | Requer unidade de análise e mediação humana | De difícil estruturação e transferência |
| Frequentemente quantificável | Exige consenso sobre significado | Frequentemente tácito |

**Processamento de dados:** Transformação de dados brutos em informação útil.

## 2. Sistemas Numéricos

### Sistemas Posicionais
- **Sistema Decimal:** Base 10 con dígitos {0,1,2,3,4,5,6,7,8,9}
- **Representação:** Número = Σ(dígito × base^posição)
- **Exemplo:** 352 = 3×10² + 5×10¹ + 2×10⁰

### Sistema Binário (Base 2)
- **Dígitos:** Apenas {0,1}
- **Conversão:** (1101)₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = (13)₁₀
- **Contagem:** 0, 1, 10, 11, 100, 101, 110, 111, 1000...

### Unidades de Medida
- **Bit (b):** Menor unidade de informação
- **Nibble:** 4 bits
- **Byte (B):** 8 bits = 2 nibbles
- **Word:** 16 bits = 2 bytes

### Sistema Hexadecimal (Base 16)
- **Dígitos:** {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
- **Onde:** A=10, B=11, C=12, D=13, E=14, F=15
- **Conversão rápida:** 1 dígito hex = 4 bits (1 nibble)
- **Notação:** 0xABCD ou ABCDh

## 3. Operações Matemáticas em Sistemas de Numeração

### Conversão de Bases
- **Binário → Decimal:** Somar potências de 2
- **Decimal → Binário:** Usar tabela de potências de 2
- **Binário ↔ Hexadecimal:** Agrupar/separar de 4 em 4 bits

### Operações Aritméticas Binárias

#### Adição Binária
```
Tabela verdade:
0 + 0 = 0 (carry 0)
0 + 1 = 1 (carry 0)
1 + 0 = 1 (carry 0)
1 + 1 = 0 (carry 1)
```

#### Subtração Binária (Complemento de 2)
- **Processo:** C₂ = C₁ + 1
- **C₁:** Inverter todos os bits
- **Subtração:** A - B = A + C₂(B)

#### Multiplicação e Divisão
- **Multiplicação:** Tabela verdade bit a bit + somas sucessivas
- **Divisão:** Processo similar ao decimal, mais custoso computacionalmente

## 4. Processamento de Dados

### Dados Digitais
- **Definição:** Representação computacional de dados extracomputacionais
- **Formato:** Sempre numérico em bits e bytes
- **Conversão:** Todo dado deve ser convertido em sequência de 0s e 1s

### Tipos de Dados e Conversão

#### Caracteres (Texto)
- **ASCII:** American Standard Code for Information Interchange
- **Processo:** Tabela converte cada caractere em número binário

#### Imagens
- **Pixel:** Menor unidade da imagem (equivale a um bit da imagem)
- **Quantificação:** Cada pixel recebe valores numéricos para cor e intensidade
- **Processo:** Dividir imagem em pixels → converter em números binários

#### Sons e Vídeos
- Estratégias similares às imagens
- Conversão em coleções de dígitos binários

### Tipos de Processamento
- **Batch (Lotes):** Processamento programado em horários determinados
- **Tempo Real:** Processamento imediato quando necessário

## 5. Ciclo de Vida da Informação

### Etapas do Processamento (Ghazal et al., 2021)

1. **Aquisição**
   - Primeiro contato com dado bruto
   - Uso de transdutores/sensores
   - Conversão de grandeza física em dado digitalizável

2. **Pré-processamento**
   - Teste de inconsistências e erros
   - Padronização de escalas
   - Eliminação de dados errôneos

3. **Análise**
   - Aplicação de algoritmos de processamento
   - Técnicas de ciência de dados
   - Machine learning e deep learning

4. **Serviço**
   - Utilização para tomada de decisão
   - Consumo do resultado do processamento

### Segurança da Informação no Ciclo de Vida

#### Fases Críticas:
- **Produção/Manipulação:** Erros de algoritmo, alterações propositais
- **Armazenamento:** Falhas de hardware, instabilidade de rede, acessos indevidos
- **Consumo:** Múltiplos acessos e utilizações
- **Descarte:** Eliminação segura e tempestiva

#### Importância:
- Preservação da autenticidade dos dados digitais
- Manutenção da privacidade e confidencialidade
- Qualidade do conhecimento gerado
- Liberação de recursos computacionais

## Conclusão

Esta aula estabeleceu os fundamentos sobre:
- A diferenciação entre dados, informação e conhecimento
- Como os sistemas numéricos (especialmente binário e hexadecimal) funcionam
- As operações matemáticas básicas em computação
- Os processos de conversão de dados extracomputacionais em dados digitais
- O ciclo completo de processamento e vida útil da informação