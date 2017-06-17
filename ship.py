import pygame 
import math
import bullet
class ship:
	def __init__(self, x , y, angle):
		self.x = x
		self.y = y
		self.angle = angle
		laser = bullet.bullet()
	def checkAngle(self):
		return self.angle
		print("CheckAngle works") 
	def check(self):
		return(str(self.x,self.y,self.angle)) 
	def forward(self,angle):
		print("worked angle", self.angle)
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 1) 
		self.y = self.y + (math.sin(angler) * 1)	
		print(self.x,self.y)
	def backward(self,angle):
		angle = math.radians(self.angle)
		self.x = self.x + (math.cos(angle) *-1)
		self.y = self.y + (math.sin(angle) *-1) 
		print(self.x,self.y)
	def changeAngle(self,angle):
		print("Change is working") 
		self.angle += 10
		print(self.angle) 
	def shoot(self,angle):
		print("shooty mcshoot")
		angle = self.angle
		laser.move(self.angle) 
