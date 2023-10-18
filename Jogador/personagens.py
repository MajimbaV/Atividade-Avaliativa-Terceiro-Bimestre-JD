from equipamentos.Armaduras.armadura import *
from equipamentos.Armamentos.arma import *
import pygame
from pygame.locals import *

class Personagem:
	def __init__(self):
		self.armamento = dict_Arma[0]
		self.armadura = dict_Armadura[0]
		self.stamina = 50
		self.vida = 100 + self.armadura.DEF
		self.pos = [0, 0]
		self.velocidade = 1
		self.defendendo = False
		
	def andar(self):
		# if keys[pygame.K_RIGHT]:
		# 	self.pos[0] += self.velocidade
		# if keys[pygame.K_LEFT]:
		# 	self.pos[0] -= self.velocidade
		# if keys[pygame.K_UP]:
		# 	self.pos[1] -= self.velocidade		
		# if keys[pygame.K_DOWN]:
		# 	self.pos[1] += self.velocidade
			print ("O Jogador Andou")
		
	def atacar(self):
		# if keys[pygame.z] and not self.defendendo:
		if not self.defendendo:
			return print ("O Jogador Atacou")
		else:
			return print("O Jogador não atacou")
		
	def defender(self):
		self.defendendo = True
		self.pos = self.pos
		print ("O Jogador está defendendo")
		
	def abrir_inventario(self):
		print(f'''Inventário:
	Arma: {self.armamento.Nome} ({self.armamento.Descricao})
	Armadura: {self.armadura.Nome} ({self.armadura.Descricao})''')

	def consumir(self):
		print ("O Jogador usou o Consumível")
  
class Guerreiro(Personagem):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[1]
		self.armadura = dict_Armadura[1]
		self.vida += self.armadura.DEF
		self.velocidade = 1
		self.stamina = 60

class Mago(Personagem):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[2]
		self.armadura = dict_Armadura[2]
		self.vida += self.armadura.DEF
		self.velocidade = 1.5
		self.stamina = 100
    
class Arqueiro(Personagem):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[3]
		self.armadura = dict_Armadura[3]
		self.vida += self.armadura.DEF
		self.velocidade = 2
		self.stamina = 80
