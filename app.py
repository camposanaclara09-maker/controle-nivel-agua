from colorama import Fore, Style, init

init()

niveis_agua = [
    (1, "Muito baixo (crítico)"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito alto (alerta)")
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel, situacao in niveis_agua:
    cor = definir_cor(nivel)
    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)

print("\nMonitoramento finalizado.")