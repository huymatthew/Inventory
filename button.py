import pygame
from event import Input

class Button():
	def __init__(self,x,y,w,h,
				colorFill=(255,255,255),
				colorOnEnter=(240,240,240),
				colorOutLine=(0,0,0)):
		self.rect = pygame.Rect(x,y,w,h)
		self.colorFill = colorFill
		self.colorOutLine = colorOutLine
		self.colorOnEnter = colorOnEnter
		self.OnEnter = False
		self.OnExit = False
		self.OnMouseDown = False
		self.OnMouseUp = False
	def Update(self,screen):
		if self.OnExit:
			self.OnExit = False
		if self.OnEnter:
			pygame.draw.rect(screen,self.colorOnEnter,self.rect)
		else:
			pygame.draw.rect(screen,self.colorFill,self.rect)
		pygame.draw.rect(screen,self.colorOutLine,self.rect,3)
		if self.rect.collidepoint((Input.mousePosition.x,Input.mousePosition.y)):
			self.OnEnter = True
			if Input.GetMouseButtonDown(0):
				self.OnMouseDown = True
			else:
				self.OnMouseDown = False
			if Input.GetMouseButtonUp(0):
				self.OnMouseUp = True
			else:
				self.OnMouseUp = False
		elif self.OnEnter:
			self.OnExit = True
			self.OnEnter = False
#pygame.init()
#screen = pygame.display.set_mode((500,500))
#btn = Button(50,50,100,50)
#while True:
#	screen.fill((128,128,128))
#	Input.Update()
#	btn.Update(screen)
#	pygame.display.update()