import guessinggame
import hangmangame

print("Escolhe o seu jogo")
print("(1) Adivinhação (2) Forca")

try:
    game = int(input("Qual jogo você deseja jogar: "))

    if game == 1:
        guessinggame.start()
    else:
        hangmangame.start()
except:
    print("Escolha um jogo existente")