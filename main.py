import socket

while True:
    def get_ip(target_host):
        try:
            ip = socket.gethostbyname(target_host)
            return ip
        except socket.gaierror:
            print('Erro ao obter o IP para o host fornecido.')
            return None

    if __name__ == "__main__":
        target_host = input("Digite o nome do site para obter o IP: ")
        IP = get_ip(target_host)
        if IP:
            print(f'O endereço IP de {target_host} é {IP}')