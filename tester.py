import ship
import pygame
import bullet
def main():
	angle = 0
	nimbus = ship.ship(250,250,angle)
	a = nimbus.checkAngle
	#window = screen.screen(500,500)  
	#pygame.display.set_mode([window.height,window.width])
	run = True  
	while run == True:
		command = input("Enter a command")
		if command == "q":
			break 
		if command == "a":
			nimbus.forward(nimbus.angle)
			
		if command == "d":
			nimbus.backward(nimbus.angle)
		
		if command == "w":
			nimbus.changeAngle(nimbus.angle) 
		if command == "e":
			nimbus.shoot(nimbus.angle)
			
main()
