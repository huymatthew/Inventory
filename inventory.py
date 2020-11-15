from button import Button 
from DataBase import item
import pygame
from event import Input
from animation import Animation
from textMoreLow import Text
import random

class ItemSlot():
	def __init__(self,item=-1,amount=0):
		self.item = item
		self.amount = amount
	def Clear(self):
		self.item = -1
		self.amount = 0 
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("EAT!")
pygame.display.set_icon(pygame.image.load("Data/Icon/item11.ico"))

amountSlots = 27
EnterSlot = None
itemOn = -1
amountOn = 0
openTipTime = 300
fontGame = pygame.font.Font("Data/Fonts/VCR.ttf",16)
descriptionTool = Text(0,0,170,"",font="Data/Fonts/VCR.ttf",size=16)

playerEat = Animation()
playerEat.AddAnimationRange(range(1,15,1),0.1,"Data/Images/PlayerEat",name="eat",loop=False)
playerEat.AddAnimationRange(range(1,3,1),0.3,"Data/Images/PlayerIdle",name="idle")
playerEatImage = pygame.image.load("Data/Images/PlayerEat1.png")
playerCollider = pygame.Rect(650,200,112,217)
playerHungryTime = 1000
playerNeedFood = random.randrange(0,len(item),1)
playerEatSound = pygame.mixer.Sound("Data/Sounds/eat.wav")

randomTime = 0
itemRandom = -1
generate = False
eatWrong = pygame.mixer.Sound("Data/Sounds/UGH.wav")

inventory = [[Button(x * 50 + 50,y * 50 + 50,50,50,colorOutLine=(230,230,230)),ItemSlot()] for y in range(3) for x in range(9)]
Generate = Button(200,410,100,50,colorOutLine=(0,0,230),colorFill=(30,30,255),colorOnEnter=(50,50,200))
def Save(data):
	text = open("Data/Data/data.inv","w")
	text.write(data)
	text.close()
def Load():
	global inventory
	text = open("Data/Data/data.inv","r")
	data = eval(str(text.read()))
	for slot in range(len(inventory)):
		inventory[slot][1].item = data[slot][0]
		inventory[slot][1].amount = data[slot][1]
def AddItem(inventory,item,amount=1):
	add = False
	for slot in inventory:
		if add == False:
			if slot[1].item == item:
				slot[1].amount += 1
				add = True
	for slot in inventory:
		if not add:
			if slot[1].item == -1:
				slot[1].item = item
				slot[1].amount += 1
				add = True
Load()
while True:
	screen.blit(pygame.image.load("Data/Images/BackGround.png"),(-150,-150))
	Input.Update()



	if playerEat.update() != None:
		playerEatImage = playerEat.update()
	if playerHungryTime > 0:
		playerHungryTime -= 1
	if playerCollider.collidepoint((Input.mousePosition.x,Input.mousePosition.y)) and Input.GetMouseButtonDown(0):
		if itemOn == playerNeedFood:
			playerEatSound.play()
			playerEat.Play("eat")
			playerHungryTime = 1000
			playerNeedFood = random.randrange(0,len(item),1)
			amountOn -= 1
		else:
			eatWrong.play()
			eatWrong.set_volume(0.5)

	#else:
		#playerEatImage = pygame.image.load("PlayerEat1.png")
	screen.blit(playerEatImage,(650,200))
	screen.blit(pygame.transform.scale(pygame.image.load("Data/Images/textBox.png"),(128,128)),(playerCollider.x - 64,playerCollider.y - 64))
	screen.blit(pygame.transform.scale(item[playerNeedFood]['Sprite'],(64,64)),(playerCollider.x - 32,playerCollider.y - 48))
	Generate.Update(screen)


	if Generate.OnMouseDown:
		generate = True
		randomTime = 100


	if randomTime > 0:
		randomTime -= 1
		itemRandom = random.randrange(0,len(item),1)
	elif randomTime > -50:
		randomTime -= 1
	elif generate:
		generate = False
		AddItem(inventory,itemRandom,1)
	pygame.draw.rect(screen,(250,250,250),(50,400,64,64))
	pygame.draw.rect(screen,(50,50,50),(50,400,64,64),3)
	if generate:
		screen.blit(pygame.transform.scale(item[itemRandom]['Sprite'],(64,64)),(50,400))

	if Input.GetKeyDown("RETURN"):
		Load()
	if Input.GetKeyDown("SPACE"):
		data = []
		for d in inventory:
			data.append([d[1].item,d[1].amount])
		Save(str(data))
	for slot in inventory:
		slot[0].Update(screen)
		if slot[0].OnEnter:
			EnterSlot = slot
		if slot[0].OnExit:
			EnterSlot = None
		if slot[1].item > -1:
			screen.blit(pygame.transform.scale(item[slot[1].item]['Sprite'],(46,46)),(slot[0].rect.x + 2,slot[0].rect.y + 2))
	for slot in inventory:
		if slot[1].amount != 0:
			screen.blit(fontGame.render(str(slot[1].amount),True,(0,0,0)),(slot[0].rect.x + 40,slot[0].rect.y + 40))
	for slot in inventory:
		if slot[0].OnEnter:
			if openTipTime > 0:
				openTipTime -= 1
			elif slot[1].item != -1:
				pygame.draw.rect(screen,(255,255,255),(Input.mousePosition.x,Input.mousePosition.y,200,200))
				pygame.draw.rect(screen,(10,10,10),(Input.mousePosition.x,Input.mousePosition.y,200,200),2)
				screen.blit(pygame.transform.scale(item[slot[1].item]['Sprite'],(70,70)),(Input.mousePosition.x + 10,Input.mousePosition.y + 10))
				screen.blit(fontGame.render(str(slot[1].amount),True,(0,0,0)),(Input.mousePosition.x + 70,Input.mousePosition.y + 70))
				screen.blit(fontGame.render(str(item[slot[1].item]['Name']),True,(0,0,0)),(Input.mousePosition.x + 80,Input.mousePosition.y + 10))
				descriptionTool.totalText = item[slot[1].item]['Description']
				descriptionTool.x = Input.mousePosition.x + 10
				descriptionTool.y = Input.mousePosition.y + 100
				descriptionTool.update(screen)
	if EnterSlot != None:
		if Input.GetMouseButtonDown(0):
			if itemOn == -1:
				itemOn = EnterSlot[1].item
				amountOn = EnterSlot[1].amount
				EnterSlot[1].Clear()
			else:
				if EnterSlot[1].item != itemOn:
					draft = [EnterSlot[1].item,EnterSlot[1].amount]
					EnterSlot[1].item = itemOn
					EnterSlot[1].amount = amountOn
					itemOn = draft[0]
					amountOn = draft[1]
				else:
					EnterSlot[1].item = itemOn
					EnterSlot[1].amount += amountOn
					itemOn = -1
					amountOn = 0
		if Input.GetMouseButtonDown(2):
			if itemOn == -1:
				itemOn = EnterSlot[1].item
				amountOn = round(EnterSlot[1].amount/2)
				EnterSlot[1].amount -= amountOn
			else:
				if EnterSlot[1].item == -1:
					EnterSlot[1].item = itemOn
					EnterSlot[1].amount = 1
					amountOn -= 1
				else:
					if EnterSlot[1].item == itemOn:
						amountOn -= 1
						EnterSlot[1].amount += 1
	if EnterSlot == None and openTipTime < 300:
		openTipTime += 20
	if amountOn == 0:
		itemOn = -1
	if itemOn != -1:
		screen.blit(pygame.transform.scale(item[itemOn]['Sprite'],(46,46)),(Input.mousePosition.x - 23,Input.mousePosition.y-23))
	if amountOn != 0:
		screen.blit(fontGame.render(str(amountOn),True,(0,0,0)),(Input.mousePosition.x +16,Input.mousePosition.y+16))
	pygame.display.update()