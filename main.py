from Jogador.personagens import *
from Inimigos.inimigo import *



print("-"* 20, "Jogador", "-"* 20)
guerreiroteste = Guerreiro()
print(guerreiroteste.vida)

guerreiroteste.andar()
guerreiroteste.atacar()
guerreiroteste.abrir_inventario()
guerreiroteste.consumir()

print()
print("-"* 20, "Inimigo", "-"* 20)
minotauro = Minotauro()

minotauro.Seguir(guerreiroteste.pos)
minotauro.Atacar(guerreiroteste)


print(guerreiroteste.vida)

