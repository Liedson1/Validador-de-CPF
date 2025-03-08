import socket
from validar_cpf import validar_cpf

def servidor_tcp():
    # Cria o socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Binda o servidor ao endereço e porta
    server.bind(("localhost", 65432))
    server.listen()
    print("Servidor TCP aguardando conexões...")

    try:
        while True:
            conn, addr = server.accept()
            with conn:
                cpf = conn.recv(1024).decode()

                if cpf == "STOP":
                    print("\nServidor interrompido pela solicitação do cliente.")
                    conn.sendall("Servidor fechado.".encode())
                    break  # Encerra a conexão e o servidor
                
                resposta = "CPF válido" if validar_cpf(cpf) else "CPF inválido"
                print(f"[LOG] Conexão de {addr}, CPF recebido: {cpf}, Resposta: {resposta}")
                conn.sendall(resposta.encode())
    
    except KeyboardInterrupt:
        print("\nServidor interrompido manualmente. Fechando o servidor...")
    finally:
        server.close()

if __name__ == "__main__":
    servidor_tcp()
