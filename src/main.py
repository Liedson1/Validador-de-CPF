from servidor.servidor_tcp import servidor_tcp
from servidor.servidor_udp import servidor_udp
from cliente.cliente_tcp import cliente_tcp
from cliente.cliente_udp import cliente_udp

def main():
    print("\n=== Sistema de Validação de CPF ===")
    opcoes = {
        "1": ("Servidor TCP", servidor_tcp),
        "2": ("Cliente TCP", cliente_tcp),
        "3": ("Servidor UDP", servidor_udp),
        "4": ("Cliente UDP", cliente_udp),
        "5": ("Parar Servidor", None),  
    }

    while True:
        # Exibe o menu
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave} - {descricao}")

        escolha = input("Escolha uma opção: ")

        if escolha in opcoes:
            _, funcao = opcoes[escolha]
            
            if funcao is None:  
                print("Parando os servidores... Até logo!")
                break  
            else:
                funcao()  
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
