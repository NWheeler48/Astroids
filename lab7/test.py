import ship
import asteriod 
import bullet 

nimbus = ship.ship(0,0,90)
aster = asteriod.asteriod(100,100,90) 
nimbus.shoot(-300)
while True:
	command = input("please enter a key") 
	if command == "q":
		break 
	if command == "w": 
		nimbus.move("w")
	if command == "a":
		nimbus.move("a")
	if command == "s":
		nimbus.move("s")
	if command == "d":
		nimbus.move("d") 
