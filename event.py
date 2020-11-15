import pygame
import sys 
from collections import namedtuple
Vector2 = namedtuple('Vector2', 'x, y')
pygame.init()
class Event():
	def __init__(self):
		self.key_press = pygame.key.get_pressed()
		self.key_down = []
		self.key_up = []
		self.mouse_visible = True
		self.mouse_down = [False] * 3
		self.mouse_up = [False] * 3
		self.mouse_press = [False] * 3
		self.mouseWheel = 0
		self.mousePosition = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
		self.mouseMotion = Vector2((pygame.mouse.get_pos()[0] - self.mousePosition.x)/10,(pygame.mouse.get_pos()[1] - self.mousePosition.y)/10)

		self.unicode = None


	def Update(self):
		self.key_press = pygame.key.get_pressed()
		self.key_down = []
		self.key_up = []

		self.mouseWheel = 0
		self.mouse_down = [False] * 3
		self.mouse_up = [False] * 3
		self.mouseMotion = Vector2((pygame.mouse.get_pos()[0] - self.mousePosition.x)/10,(pygame.mouse.get_pos()[1] - self.mousePosition.y)/10)
		self.mousePosition = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
		self.mouse_press = pygame.mouse.get_pressed()

		self.unicode = None
		pygame.mouse.set_visible(self.mouse_visible)
		if self.mouseMotion.x > 1:
			self.mouseMotion = Vector2(1,self.mouseMotion.y)
		elif self.mouseMotion.x < -1:
			self.mouseMotion = Vector2(-1,self.mouseMotion.y)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				self.key_down.append(event.key)
				self.unicode = event.unicode
			if event.type == pygame.KEYUP:
				self.key_up.append(event.key)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.mouse_down[0] = True
				if event.button == 2:
					self.mouse_down[1] = True
				if event.button == 3:
					self.mouse_down[2] = True
				if event.button == 4:
					self.mouseWheel = 1
				if event.button == 5:
					self.mouseWheel = -1
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					self.mouse_up[0] = True
				if event.button == 2:
					self.mouse_up[1] = True
				if event.button == 3:
					self.mouse_up[2] = True
			if Input.GetKey("LALT") and Input.GetKeyDown("F4"):
				pygame.quit()
				sys.exit()

	def SeeMouse(self,scene):
		pygame.draw.line(scene.screen,(0,0,0),(self.mousePosition.x,0),(self.mousePosition.x,scene.screen.get_height()))
		pygame.draw.line(scene.screen,(0,0,0),(0,self.mousePosition.y),(scene.screen.get_width(),self.mousePosition.y))
		text = pygame.font.Font(None,16).render(str(self.mousePosition.x)+" , "+str(self.mousePosition.y),True,(0,0,0))
		scene.screen.blit(text,(self.mousePosition.x -30,self.mousePosition.y -30))
	def GetUnicode(self):
		return self.unicode

	def GetKeyDown(self,key):
		k = eval("pygame.K_" + key)
		for _key in self.key_down:
			if _key == k:
				return True
			else:
				return False
	def GetKeyUp(self,key):
		k = eval("pygame.K_" + key)
		for _key in self.key_up:
			if _key == k:
				return True
			else:
				return False
	def GetKey(self,key):
		k = eval("pygame.K_" + key)
		if self.key_press[k] == 0:
			return False
		else:
			return True
	def GetMouseButtonDown(self,button):
		return self.mouse_down[button]
	def GetMouseButtonUp(self,button):
		return self.mouse_up[button]
	def GetMouseButton(self,button):
		if self.mouse_press[button] == 1:
			return True
		else:
			return False
Input = Event()