import pygame
from event import Input
class Text():
	def __init__(self,x,y,w,text,font=None,size=24,color=(0,0,0)):
		self.x = x
		self.y = y
		self.w = w
		self.font = pygame.font.Font(font,size)
		self.color = color
		self.totalText = text
		self.text = []
	def update(self,screen):
		self.text = []
		for char in range(len(self.totalText)):
			if len(self.text) == 0:
				if self.font.size(self.totalText[0:char])[0] > self.w:
					self.text.append([self.totalText[0:char],char])
			else:
				if self.font.size(self.totalText[self.text[-1][1]:char])[0] > self.w:
					self.text.append([self.totalText[self.text[-1][1]:char],char])
		for txt in range(len(self.text)):
			screen.blit(self.font.render(self.text[txt][0],True,self.color),(self.x,self.y + txt * self.font.size("I")[1]))
		if len(self.text) > 0:
			if self.text[-1][1] < len(self.totalText):
				screen.blit(self.font.render(self.totalText[self.text[-1][1]:-1],True,self.color),(self.x,self.y + (txt + 1) * self.font.size("I")[1]))
		else:
			screen.blit(self.font.render(self.totalText,True,self.color),(self.x,self.y))
#pygame.init()
#screen = pygame.display.set_mode((500,500))
#text = Text(50,50,400,"helollsadasoiasdgafydsybcxaytbravctf")
#while True:
#	Input.Update()
#	screen.fill((128,128,128))
#	if Input.GetUnicode() != None:
		#text.totalText += Input.GetUnicode()
#	text.update(screen)
#	pygame.display.update()