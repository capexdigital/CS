# Aula 5: Introdução às Redes de Computadores

### 1.1 Conceito
- **Rede de computadores**: interligação de dispositivos capazes de se comunicar
- Dispositivos incluem: sistemas finais (servidores, desktops, laptops, celulares) e dispositivos de conexão (roteadores, switches)
- Conexão usando meios com ou sem fio (cabos ou ar)

### Classificação das Redes

#### LAN (Local Area Network)
- Rede local de propriedade privada
- Conecta hosts em escritório, prédio ou campus
- Comunicação através de pacotes de dados
- Cada máquina recebe um endereço único para identificação

#### WAN (Wide Area Network)
- Abrange maior extensão geográfica (cidade, país, mundo)
- Interliga dispositivos de conexão (switches, roteadores, modems)
- **Tipos de WAN**:
  - Ponto a ponto
  - Comutadas (combinação de WANs ponto a ponto interligadas por switches)

### Internet Privada
- Conexão entre redes cria uma "internet"
- Corporações podem interconectar LANs via WAN comutada dedicada
- Estabelece internet privada (intranet)

### 1.2 Protocolos de Comunicação
- **Função**: conjunto de regras para comunicação eficiente entre emissor e receptor
- **Elementos definidos**:
  - Identificação do emissor e receptor
  - Linguagem padronizada
  - Velocidade de transmissão (10 Mbps, 100 Mbps, 1 Gbps)
  - Mecanismos de confirmação

#### Protocolos Principais
- **IP (Internet Protocol)**: encapsula pacotes e controla conexão entre emissor e próximo ativo de rede
- **TCP (Transmission Control Protocol)**: controla transmissão fim a fim, estabelece ponte virtual entre origem e destino

### 1.3 Protocolos de Camadas
- **Conceito**: divisão da comunicação em diferentes camadas com protocolos distintos
- **Vantagem**: separação de serviços de suas implementações
- **Conexão lógica**: cada camada se comunica com sua equivalente no destino
- Camada recebe serviços da inferior e oferece serviços para a superior

---

## Tema 2 - Topologia de Redes de Computadores

### 2.1 Dispositivos Terminais ou Finais
- **Hosts**: terminais de usuário (computadores, telefones IP, Smart TVs, tablets, celulares)
- **Servidores/Gateways**: computadores de maior capacidade que fornecem informações
- **Dispositivos IoT**: atuam como terminais populando a Internet
- **Identificação**: cada dispositivo recebe endereço IP único na rede local
- **Endereço MAC**: numeração única do fabricante, acompanha dispositivo até descarte

### 2.2 Dispositivos Intermediários
#### Access Points (APs)
- Pontos de acesso sem fio
- Conectam terminais à rede wireless

#### Switches
- Conectam terminais via cabo de rede
- Guardam informações sobre equipamentos internos da LAN
- Usam protocolo ARP (Address Resolution Protocol)
- Encaminham pacotes externos para roteadores

#### Roteadores
- Conectam rede local com redes externas
- Possuem tabelas de roteamento atualizadas constantemente
- Sabem encaminhar qualquer pacote que chegue a eles

### 2.3 Pilha de Protocolos TCP/IP
- Dispositivos intermediários operam de forma transparente
- Usuários percebem conexão direta entre aplicações
- Controle transferido para camada de transporte

---

## Tema 3 - Conectividade

### 3.1 Cabeamento Metálico
- Ainda preponderante devido ao custo-benefício
- Interface típica: Ethernet (padrões internacionais)

#### Características Importantes:
- **Flamabilidade**: seleção adequada conforme caminhamento (CMX, CMP, CMR)
- **Compatibilidade eletromagnética**: proteção contra interferências
- **Tipos de cabos**:
  - UTP (Unshielded Twisted Pair): sem blindagem
  - FTP/STP (Foiled/Shielded Twisted Pair): blindados
- **Categorias**: Cat.5, Cat.5e, Cat.6 (determinam velocidade máxima)

### 3.2 Cabeamento Óptico
- **Princípio**: condução de luz através de dutos vítreos
- **Estrutura**: núcleo vítreo + casca + proteção polimérica
- **Tipos**:
  - **Multimodo**: menor custo, maior atenuação, distâncias curtas
  - **Monomodo**: maior qualidade, menor atenuação, longas distâncias
- **Vantagens**: imunidade a ruídos eletromagnéticos, alta velocidade
- **Limitações**: restrições mecânicas de curvatura

### 3.3 Redes Sem Fio
- **Princípio**: modulação de ondas eletromagnéticas (OEM)
- **Processo**: modulação da portadora → transmissão → demodulação
- **Exemplo**: BPSK (Binary Phase Shifting Keying)

#### WiFi (IEEE 802.11)
- **Frequências**: 2,4GHz e 5GHz
- **2,4GHz**: 3 canais não interferentes, maior penetração
- **5GHz**: até 165 canais, menor penetração
- **Limitações**: densidade de usuários, probabilidade de colisão

---

## Tema 4 - Internet

### 4.1 Definição
- **Conceito 1**: rede mundial conectando milhões de terminais
- **Conceito 2**: rede que permite troca de dados entre aplicações distribuídas
- **Estrutura**: levemente hierárquica (ISPs locais, regionais, nacionais, internacionais)
- **Web ≠ Internet**: WWW é apenas um serviço que opera sobre a Internet

### 4.2 Histórico
- **1957**: Origem militar (reação ao Sputnik)
- **1968**: Criação da ARPANET (resistência a ataques nucleares)
- **1975**: ~2.000 usuários acadêmicos
- **1979**: Primeiro provedor comercial
- **1983**: Padronização TCP/IP
- **1989**: Berners-Lee cria World Wide Web
- **1994**: Dezenas de milhões de terminais conectados

### Fases da Internet:
1. **Militar/Acadêmica**: troca de mensagens e arquivos
2. **WWW**: repositórios de arquivos online
3. **Redes Sociais**: maior demanda de banda (imagens/vídeos)

### 4.3 Crescimento
- Crescimento exponencial após 1983
- Absorção de redes locais
- IETF mantém padrões (TCP, HTTP, SMTP)
- Uso para WANs privadas e telecomunicações

### 4.4 Funcionamento
#### Estrutura Hierárquica:
- **Terminal** → **ISP Local** → **ISP Regional** → **Backbone** → **Destino**
- **Redundância**: múltiplos caminhos entre dois pontos
- **VPNs**: controle de caminho virtual
- **NAT**: tradução de endereços para reuso

---

## Tema 5 - Principais Conceitos da Internet e WWW

### 5.1 Endereçamento IP

#### IPv4
- 32 bits divididos em 4 blocos (bytes)
- Notação decimal pontilhada (ex: 192.168.1.1)
- Limitação: alguns milhões de endereços
- **Endereços públicos**: únicos na Internet
- **Endereços internos**: gerenciados por roteador local via NAT

#### IPv6
- Solução para limitação do IPv4
- Acomoda crescimento de dispositivos IoT

### 5.2 Navegação na Internet - HTTP
- **HTTP/HTTPS**: protocolo de comunicação cliente-servidor
- **HTML**: linguagem para construção de hipertextos
- **URL/URI**: localização de recursos
- **DNS**: tradução de domínios para endereços IP
- **Browser**: aplicação cliente que gerencia o processo

#### Processo de Navegação:
1. Usuário insere domínio
2. DNS traduz para IP
3. Browser envia requisição GET
4. Servidor retorna código HTML
5. Navegação através de hipertextos

### 5.3 E-mail
- **Princípio**: store-and-forward (armazenar e encaminhar)
- **Identificação**: usuário@domínio.com
- **Protocolos**: SMTP, POP, IMAP
- Precedeu a criação da WWW