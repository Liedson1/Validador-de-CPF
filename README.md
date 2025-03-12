#Sistema de Validação de CPF - Cliente/Servidor (TCP e UDP)
Este projeto é uma implementação de um sistema de validação de CPF utilizando os protocolos TCP e UDP em Python.
A aplicação cliente envia um número de CPF e o servidor realiza a validação, retornando se o CPF é válido ou não.
O projeto consiste em requisito para obtençao de nota da disciplina Sistemas Distribuídos ministrada pelo professor Tercio Silva.

📂 ##Estrutura do Projeto
projeto-cpf/
├── cliente/

│   ├── cliente_tcp.py

│   └── cliente_udp.py

├── servidor/

│   ├── servidor_tcp.py
│   └── servidor_udp.py
├── utils/
│   └── validar_cpf.py
├── main.py
└── README.md

🚀 ##Tecnologias Utilizadas
- Python 3
- Sockets (TCP e UDP)
  
⚙️ ##Como Rodar o Projeto
**Clone o repositório:**
git clone https://github.com/seuusuario/projeto-cpf.git
cd projeto-cpf
**Execute o arquivo principal:**
python main.py
**Escolha a opção desejada no menu:**
1 - Servidor TCP
2 - Cliente TCP
3 - Servidor UDP
4 - Cliente UDP
5 - Parar Servidor

📝 ##Como Funciona
**Servidor:** Aguarda conexões de clientes e valida o CPF recebido.
**Cliente:** Envia o CPF para o servidor e aguarda a resposta.
**Validação:** A verificação é realizada utilizando um algoritmo que verifica os dígitos verificadores.

🚩 ##Finalizando o Servidor
Para encerrar o servidor, digite: STOP
Isso enviará uma solicitação para o servidor parar e exibir uma mensagem de encerramento.

## Desenvolvedores
José Vinicius Cavalcante Soares - 22112113
Liedson da Silva Santos - 22110823
Thalia de Oliveira Santos - 21110245
