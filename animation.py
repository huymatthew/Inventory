import pygame
class Animation():
	def __init__(self):
		self.play = None
		self.pauseTime = 0
		self.startTime = 0
		self.animation = []
		self.loop = True
	def Play(self,name):
		for animation in self.animation:
			if animation[1] == name:
				self.play = animation[0]
				self.loop = animation[2]
				self.startTime = pygame.time.get_ticks()/1000
	def AddAnimation(self,anim,name = None,loop=True):
		if name == None:
			name = "animation" + str(len(self.animation) - 1)
		self.animation.append([anim,name,loop]);
	def AddAnimationRange(self,_range,tick,anim,name = None,loop=True):
		if name == None:
			name = "animation" + str(len(self.animation) - 1)
		animation = []
		for i in _range:
			animation.append([pygame.image.load(anim + str(i) + ".png"),i * tick])

		self.animation.append([animation,name,loop]);
	def update(self):
		if self.play != None:
			for anim in self.play:
				if anim[1] <= pygame.time.get_ticks()/1000 - self.startTime and pygame.time.get_ticks()/1000 - self.startTime < anim[1] + 0.01:
					return anim[0]
			if pygame.time.get_ticks()/1000 - self.startTime > self.play[len(self.play)-1][1] and self.loop:
				if self.play[2]:
					self.startTime = pygame.time.get_ticks()/1000