# Python Class Practice
# Written by: Mike Graziano
# Version: -

"""Goal of this program is to practice developing classes to be used in the Fashion Frame program."""

class ColorCell:
	def __init__(self,red,blue,green):
		self.redvalue = red	
		self.greenvalue = green
		self.bluevalue = blue
		self.hexvalue = red*(16**4)+green*(16**2)*blue

	def print_RGB(self):
		print("{0:d},{1:d},{2:d}".format(self.redvalue,self.greenvalue,self.bluevalue))

class ColorPalette:
	def __init__(self,name):
		self.name = name
		self.palette = [[ColorCell(0,0,0) for y in range(5)] for x in range(18)]
 
test = ColorCell(100,255,25)
print("The color that I created has a red value of {0:d}, a green value of {1:d}, and a blue value of {2:d}. \n The hex value for this value is 0x{3:X}".format(test.redvalue,test.bluevalue,test.greenvalue,test.hexvalue))

test.print_RGB()

anothertest = ColorPalette("fakename")
for color in anothertest.palette[0]: color.print_RGB() 

