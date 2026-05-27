# Atividade em Python - Agenda 11

# Controle de Níveis de Água utilizando a biblioteca colorama

# Importação da biblioteca colorama

from colorama import Fore, Style, init

# Criando listas conforme agenda 9:

lista_niveis = ["Nível Crítico", "Nível Baixo", "Nível Moderado", "Nível Bom", "Nível Máximo"]

# Criando lista de mensagens, situação e status:
nivel0 = "Nível muito baixo     "
nivel1 = "Nível Baixo           "
nivel2 = "Nível médio           "
nivel3 = "Nível alto            "
nivel4 = "Nível muito alto      "

status0 = "Crítico   "
status1 = "Atenção1  "
status2 = "Atenção2  "
status3 = "Ideal     "
status4 = "transbordo"

cor0 = "VERMELHO"
cor1 = "AMARELO "
cor2 = "VERDE   "
cor3 = "CIANO   "
cor4 = "AZUL    "

# Verificando o nível da água:
nivel = int(input("Insira um número entre 0 e 4: "))

# Imprimir cabeçalho:
print(f"{'Nivel do reservatório':<10} | {'Situação':<9} | {'STATUS'}")
print("---------------------------------------------")

# Condição if para checar o nível da água e imprimir a mensagem de alerta:
if nivel == 0:
    print(nivel0 + "| " + status0 + "| " + Fore.RED + cor0 + Style.RESET_ALL)

elif nivel == 1:
    print(nivel1 + "| " + status1 + "| " + Fore.YELLOW + cor1 + Style.RESET_ALL)
    
elif nivel == 2:
    print(nivel2 + "| " + status2 + "| " + Fore.GREEN + cor2 + Style.RESET_ALL)
    
    
elif nivel == 3:
    print(nivel3 + "| " + status3 + "| " + Fore.CYAN + cor3 + Style.RESET_ALL)
    
    
elif nivel == 4:
    print(nivel4 + "| " + status4 + "| " + Fore.BLUE + cor4 + Style.RESET_ALL)
    
    
else:
    print("Nível estável" + Style.RESET_ALL)
    status_bold = f"\033[1m\033[0m"


# FIM