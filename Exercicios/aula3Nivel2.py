# Exercício de calculadora de IMC

print("Bem vindo a calculadora de IMC")

nome = input("Digite seu nome: ")

altura = float(input("Agora digite sua altura: "))
peso = float(input("E agora digite o seu peso: "))

imc = peso / (altura**2)

print(nome, "Seu IMC é: ", imc)