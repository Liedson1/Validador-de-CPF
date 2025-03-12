# Sistema de Validação de CPF - Cliente/Servidor (TCP e UDP)

Este projeto é uma implementação de um sistema de validação de CPF utilizando os protocolos TCP e UDP em Python.
A aplicação cliente envia um número de CPF e o servidor realiza a validação, retornando se o CPF é válido ou não.

Este projeto é um requisito para obtenção de nota na disciplina **Sistemas Distribuídos**, ministrada pelo professor **Tércio Silva**.

---

## 📂 Estrutura do Projeto
```
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
```

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Sockets (TCP e UDP)**

---

## ⚙️ Como Rodar o Projeto
### 1️⃣ Clone o repositório:
```sh
git clone https://github.com/seuusuario/projeto-cpf.git
cd projeto-cpf
```
### 2️⃣ Execute o arquivo principal:
```sh
python main.py
```
### 3️⃣ Escolha a opção desejada no menu:
```
1 - Servidor TCP
2 - Cliente TCP
3 - Servidor UDP
4 - Cliente UDP
5 - Parar Servidor
```

---

## 📝 Como Funciona
### 🖥️ Servidor
- Aguarda conexões de clientes e valida o CPF recebido.
- O servidor pode operar em dois modos: **TCP** e **UDP**.

### 💻 Cliente
- Envia o CPF para o servidor e aguarda a resposta.
- Pode escolher entre **TCP** ou **UDP** para comunicação.

### ✅ Validação
- A verificação é realizada utilizando um algoritmo que valida os dígitos verificadores do CPF.

### 📜 Menu de Opções
O programa principal (`main.py`) exibe um menu para que o usuário escolha a funcionalidade desejada:
```python
1 - Servidor TCP
2 - Cliente TCP
3 - Servidor UDP
4 - Cliente UDP
5 - Parar Servidor
```
- Cada opção executa a respectiva funcionalidade.
- A opção `5` encerra o programa.

---

## 🚩 Finalizando o Servidor
- Existem duas formas de encerrar o servidor:
  1. **Digitando `STOP`**: Isso enviará uma solicitação para o servidor parar e exibir uma mensagem de encerramento.
  2. **Interrompendo manualmente (`Ctrl + C`)**: O servidor será encerrado através de uma interrupção manual no terminal.

---

## 👥 Desenvolvedores
- **José Vinicius Cavalcante Soares** - 22112113
- **Liedson da Silva Santos** - 22110823
- **Thalia de Oliveira Santos** - 21110245



## Desenvolvedores
José Vinicius Cavalcante Soares - 22112113

Liedson da Silva Santos - 22110823

Thalia de Oliveira Santos - 21110245
