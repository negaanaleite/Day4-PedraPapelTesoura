import random 
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagem_jogo = [pedra,papel,tesoura]

sua_escolha = int(input("Qual a sua escolha? Digite 0 para pedra, 1 para papel, 2 para tesoura.\n"))
print(imagem_jogo[sua_escolha])

maquina_escolha = (random.randint(0, 2))
print("Escolha da Máquina")
print(imagem_jogo[maquina_escolha])

if sua_escolha >= 3 or maquina_escolha< 0:
  print("Você digitou o numero errado. PERDEDOR")
elif sua_escolha == 0 and maquina_escolha == 2:
  print(" VENCEDOR!")
elif maquina_escolha ==0 and sua_escolha == 2:
  print("PERDEDOR!")
elif maquina_escolha > sua_escolha: 
  print("PERDEDOR!")
elif sua_escolha <  maquina_escolha: 
  print("VENCEDOR!")
elif maquina_escolha == sua_escolha:
  print("EMPATE")