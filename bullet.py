import ship 
class bullet:
	def __intit__(self):
		print("bullet is working")
		nimbus = ship.ship(250,250,0) 
		self.x = nimbus.x 
		self. y = nimbus.y	
		self.angle = nimbus.angle
	def move(self,angle):
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 10) 
		self.y = self.y + (math.sin(angler) * 10)	
		print(self.x,self.y) 
		
