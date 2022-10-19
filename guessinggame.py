def start():
    import random

    print("Bem vindo ao jogo de Adivinhação!")

    secret_number = random.randrange(0, 101)
    points = 1000

    print("Qual nível de dificuldade você deseja jogar:")
    print("(1) Fácil (2) Médio (3) Difícil")

    try:
        level = int(input("Digite o nível: "))
    except:
        print("Escolha uma difículdade valida")
        exit()

    if level == 1:
        tries = 20
    elif level == 2:
        tries = 10
    else:
        tries = 5

    for count in range(0, tries):
        print('')
        print(f'Rodada {count + 1} de {tries}')

        user_try = input('Digite um número de 1 a 100: ')
        print(f'Você digitou {user_try}')

        try:
            user_try = int(user_try)
            if secret_number == user_try:
                print(f'Você acertou e fez {points} pontos')
                break
            else:
                print('Você errou')
                if user_try > secret_number:
                    print('Tente um número menor')
                else:
                    print('Tente um número maior')

                lose_points = abs(secret_number - user_try)
                points = points - lose_points
        except:
            print('Digite um número válido')


if __name__ == '__main__':
    start()
