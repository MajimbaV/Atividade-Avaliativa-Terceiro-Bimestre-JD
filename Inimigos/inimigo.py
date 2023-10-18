from Jogador.personagens import *
import random
import pygame
class Inimigo:
  def __init__(self):
    self.vida = 0
    self.ataque = 0
    self.pos = [0, 0]
    self.velocidade = 1

  def Atacar(self, jogador):
    hitbox = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
    hitbox.x = self.pos[0]
    hitbox.y = self.pos[1]
    print("O Inimigo atacou")
    if hitbox.collidepoint(jogador.pos):
      if not jogador.defendendo:
        jogador.vida -= self.ataque
        print(f"O Inimigo causou {self.ataque} dano")
      else:
        print("O Jogador Defendeu")


  def Seguir(self, playerpos):
    if self.pos[0] < playerpos[0]:
      self.pos[0] += self.velocidade // 2
      print ("O Inimigo seguiu para a direita")
    if self.pos[0] > playerpos[0]:
      self.pos[0] -= self.velocidade // 2
      print ("O Inimigo seguiu para a esquerda")
    if self.pos[1] < playerpos[1]:
      self.pos[1] += self.velocidade // 2
      print ("O Inimigo seguiu para cima")
    if self.pos[1] > playerpos[1]:
      self.pos[1] -= self.velocidade // 2
      print ("O Inimigo seguiu para baixo")
    if self.pos == playerpos:
      print ("O Inimigo encontrou-se com o jogador")

class Minotauro(Inimigo):
	def __init__(self):
		super().__init__()
		self.vida = 300
		self.ataque = 10
		self.pos = [0, 0]
		self.velocidade = 0.5


class Goblin(Inimigo):
	def __init__(self):
		super().__init__()
		self.vida = 20
		self.ataque = 2
		self.pos = [0, 0]
		self.velocidade = 1
