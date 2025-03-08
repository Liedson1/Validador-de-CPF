import socket
from validar_cpf import validar_cpf

def servidor_udp():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    server.bind(("localhost", 65435))
    print("Servidor UDP aguardando mensagens...")

    try:
        while True:
            
            cpf, addr = server.recvfrom(1024)
            mensagem = cpf.decode()

            if mensagem == "STOP":
                print("\nServidor interrompido pela solicitação do cliente.")
                server.sendto("Servidor fechado.".encode(), addr)
                break  

            
            resposta = "CPF válido" if validar_cpf(mensagem) else "CPF inválido"
            print(f"[LOG] Conexão de {addr}, CPF recebido: {mensagem}, Resposta: {resposta}")
            
            
            server.sendto(resposta.encode(), addr)
    
    except KeyboardInterrupt:
        print("\nServidor interrompido manualmente. Fechando o servidor...")
    finally:
        server.close()

if __name__ == "__main__":
    servidor_udp()
