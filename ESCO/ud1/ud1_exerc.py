# Constantes
IVE = 21

# Variables
matricula = input("Matrícula do vehículo: ")
prezo_hora_man_de_obra = float(input("Prezo da hora de man de obra: "))
horas_traballadas = float(input("Horas traballadas: "))
custo_pezas = float(input("Custo das pezas (€): "))

# Cálculos
custo_man_de_obra = float(prezo_hora_man_de_obra * horas_traballadas)
base = custo_man_de_obra + float(custo_pezas)
calculo_ive = base * (IVE / 100)
custo_total = base + calculo_ive

horas = int(horas_traballadas)
minutos = round(((horas_traballadas) % 1) * 60)
tempo = f"Tempo: {horas} h {minutos} min"

# Salida por pantalla
print("\n")
print(f"ORZAMENTO - {matricula}\n")
print(f"{'Man de obra ':<25} {custo_man_de_obra:>20.2f} €")
print(f"{'Pezas':<25} {custo_pezas:>20.2f} €")
print(f"{'-' * 45}")
print(f"{'Base ':<25} {base:>20.2f} €")
print(f"{f'IVE ({IVE}%)':<25} {calculo_ive:>20.2f} €")
print(f"{'-' * 45}")
print(f"{'TOTAL ':<25} {custo_total:>20.2f} €\n")
print(tempo)

