# Exercício de cálculo de média
nome = input('Digite seu nome: ')
print('Bem vindo {}! Vamos verificar se você está aprovado!'.format(nome))

av1 = float(input('Digite sua nota da AV1: '))
av2 = float(input('Digite sua nota da AV2: '))
av3 = float(input('Digite sua nota da AV3: '))

media = (av1 + av2 + av3) / 3

if media >= 7.0:
    print('Sua média é: {}. Parabéns {}! Você está aprovado!'.format(media, nome))
else:
    if media <= 6.0:
        print('Sua média é: {}. Que pena {}, Você foi reprovado!'.format(media, nome))
    else:
        print('Sua média é: {}. Atenção {}! Você está de recuperação! Estude mais.'.format(media, nome))