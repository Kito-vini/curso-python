# Exercício de cálculo de custo médio de combustpivel

combustivelGasto = int(input("Digite a quantidade gasta de combustível: "))
kilometrosPercorrido = int(input("Digite a quantidade de KM percorridos: "))

custoMedio = kilometrosPercorrido / combustivelGasto

print("O custo médio de combustível é de {}Km/l".format(custoMedio))