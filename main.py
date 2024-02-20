import sys
import socket

def get_ip(target_host):
    try:
        ip = socket.gethostbyname(target_host)
        return ip
    except:
        print('IP inválido')
        sys.exit()

if __name__ == "__main__":
    read_hostname = sys.argv[1]
    IP = get_ip(read_hostname)
    print(f'O endereço IP de {read_hostname} é {IP}')

# Exemplos de uso:
# python main.py google.com