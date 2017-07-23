# Python Class Practice
# Written by: Mike Graziano
# Version: -

"""Goal of this program is to practice developing classes to be used in the Fashion Frame program."""

class ColorCell:
        def __init__(self,red,green,blue):
                self.redvalue = red	
                self.greenvalue = green
                self.bluevalue = blue
                self.hexvalue = red*(16**4)+green*(16**2)+blue
                self.RGB = "({0:d},{1:d},{2:d})".format(red,green,blue)

        def update(self,new_red,new_green,new_blue):
                self.redvalue = new_red
                self.greenvalue = new_green
                self.bluevalue = new_blue
                self.hexvalue = self.redvalue*(16**4)+self.greenvalue*(16**2)+self.bluevalue
                self.RGB = "({0:d},{1:d},{2:d})".format(new_red,new_green,new_blue)

class ColorPalette:
        def __init__(self,name):
                self.name = name
                self.palette = [[ColorCell(0,0,0) for y in range(5)] for x in range(18)]
 
test = ColorCell(100,255,25)
print("The color that I created has a red value of {0:d}, a green value of {1:d}, and a blue value of {2:d}. \n The hex value for this value is 0x{3:X}".format(test.redvalue,test.bluevalue,test.greenvalue,test.hexvalue))

anothertest = ColorPalette("fakename")
for color in anothertest.palette[0]: print(color.RGB,end=" ")
print()

for color in anothertest.palette[0]:
        color.update(100,100,100)
        print(color.RGB,end=" ")
print()

#anothertest.palette[0][0].update(100,100,100)
#print(anothertest.palette[0][0].RGB)
