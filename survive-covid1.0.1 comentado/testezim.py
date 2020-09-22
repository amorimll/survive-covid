import random

itens = ["feijao", "arroz", "gel", "covid"]

running = True
while running == True: 
    itemEscolhido = random.choice(itens)

    print(itemEscolhido)
