# Construindo a parte inicial: 

print("Seja muito bem vindo ao quiz da Jullia")

answer_user = input("Quer começar? (S/N) ").upper()

# GANHE PONTOS DO QUANTO VOCE ACERTAR

if answer_user != "S":
    quit()

score = 0   

print("Começando...")    

# PERGUNTAS:

# 01
print("1. Quem desenvolveu o jogo GTA? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ").upper()
if answer_1 == "A":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 02
print("2. Qual o nome do protagonista da série 'The Legend of Zelda'? \n (A) Zelda \n (B) Ganon \n (C) Link \n (D) Navi \n")
answer_2 = input("Resposta: ").upper()
if answer_2 == "C":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 03
print("3. Qual dessas empresas criou o console PlayStation? \n (A) Nintendo \n (B) Sony \n (C) Microsoft \n (D) Sega \n")
answer_3 = input("Resposta: ").upper()
if answer_3 == "B":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 04
print("4. No jogo 'Minecraft', qual criatura explode ao chegar perto do jogador? \n (A) Zombie \n (B) Enderman \n (C) Skeleton \n (D) Creeper \n")
answer_4 = input("Resposta: ").upper()
if answer_4 == "D":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 05
print("5. Qual é o gênero do jogo 'League of Legends'? \n (A) FPS \n (B) MOBA \n (C) RPG \n (D) Battle Royale \n")
answer_5 = input("Resposta: ").upper()
if answer_5 == "B":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 06
print("6. Qual é a principal mascote da SEGA? \n (A) Mario \n (B) Crash Bandicoot \n (C) Sonic \n (D) Pac-Man \n")
answer_6 = input("Resposta: ").upper()
if answer_6 == "C":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 07
print("7. Qual destes jogos é um Battle Royale? \n (A) Fortnite \n (B) FIFA \n (C) God of War \n (D) Tetris \n")
answer_7 = input("Resposta: ").upper()
if answer_7 == "A":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 08
print("8. Como se chama o vilão principal que sequestra a Princesa Peach? \n (A) Donkey Kong \n (B) Bowser \n (C) Wario \n (D) Ridley \n")
answer_8 = input("Resposta: ").upper()
if answer_8 == "B":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")

# 09
print("9. Qual jogo de blocos foi criado por Alexey Pajitnov em 1984? \n (A) Minecraft \n (B) Roblox \n (C) Tetris \n (D) Lego Worlds \n")
answer_9 = input("Resposta: ").upper()
if answer_9 == "C":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")     

# 10
print("10. Qual é o nome do console híbrido da Nintendo que pode ser usado na TV ou como portátil? \n (A) Game Boy \n (B) Nintendo Switch \n (C) Wii U \n (D) Nintendo DS \n")
answer_10 = input("Resposta: ").upper()

if answer_10 == "B":
    print("CORRETO!")
    score = score + 1
else:
    print("RESPOSTA ERRADA!")   

print("O quiz chegou ao fim... ")      
print(f"Sua pontuação foi de: {score}/10 ")