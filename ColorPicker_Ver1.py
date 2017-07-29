# Warframe Color Picker Program
# Written by: Mike Graziano
# Version: 1.2

class ColorCell:
        def __init__(self,name,red,green,blue):
                self.name = name
                self.red = red
                self.green = green
                self.blue = blue
                self.hex = red*(16**4)+green*(16**2)+blue
                self.RGBtext = "({0:d},{1:d},{2:d})".format(red,green,blue)
                self.HEXtext = "0x{0:X}".format(self.hex)

        def update(self,name,red,green,blue):
                self.name = name
                self.red = red
                self.green = green
                self.blue = blue
                self.hex = red*(16**4)+green*(16**2)+blue
                self.RGBtext = "({0:d},{1:d},{2:d})".format(red,green,blue)
                self.HEXtext = "0x{0:X}".format(self.hex)

class ColorPalette:
        def __init__(self, name):
                self.name = name
                self.palette = [[ColorCell("Blank",0,0,0) for y in range(5)] for x in range(18)]

""" Initialize major variables:
        * List object "file_list" holds all the names of the standard Warframe pallettes.
        * Dictionary object "archive_pallette" holds the Python representation of the Warframe pallettes.
        * List object "test_colors" holds dictionaries of the colors to be tested. """
file_list = []
with open("Initialize.txt", "r") as file:
        file_size = int(file.readline().lstrip("Names =  ").rstrip("\n"))
        for line in range(file_size):
                file_list.append(file.readline().rstrip("\n"))
archive_palette = []
test_colors = []

# Creates archive pallette dictionary from text files
for item in file_list:
        file_palette = ColorPalette(item)
        with open(item + ".txt", "r") as file:
                for column in range(0, 5, 1):
                        for row in range(0, 18, 1):
                                # Save line from open file
                                line_buffer = file.readline().rstrip("\n").split(",")

                                # Error checking before proceeding to the integer initialization
                                if len(line_buffer) != 6:
                                        quit(print("Incorrect number of elements at cell {0:s},{1:s} in {2:s}".format(line_buffer[0], line_buffer[1], item)))

                                # Initializes everything but "HEX" value to integer
                                for index in range(len(line_buffer)):
                                        if index != len(line_buffer)-1:
                                                line_buffer[index] = int(line_buffer[index], 10)

                                # Check that the RGB values & HEX value are equivalent
                                if int(line_buffer[5], 0) != line_buffer[2]*(16**4) + line_buffer[3]*(16**2) + line_buffer[4]*(16**0):
                                        quit(print("Error located at cell {0:d},{1:d} in {2:s}".format(line_buffer[0], line_buffer[1], item)))

                                #Add values to the pallette matrix
                                file_palette.palette[row][column].update(item+" ({0:d},{1:d})".format(row,column),line_buffer[2],line_buffer[3],line_buffer[4])

        archive_palette.append(file_palette)

# Create test colors list from "Test_Input.txt" file
with open("Test_Input.txt", "r") as file:
        for line in file:
                line_buffer = line.rstrip().split(",")
                test_colors.append(ColorCell(line_buffer[0],int(line_buffer[1][0:4], 0),int(line_buffer[1][0:2] + line_buffer[1][4:6], 0),int(line_buffer[1][0:2] + line_buffer[1][6:8], 0)))

# Determine the best approximation for each color and output it to the "Test_Output.txt" file
with open("Test_Output.txt", "w") as file:
        for color in test_colors:
                approximation = ColorCell("Blank",0,0,0)
                approx_delta = 0
                for item in archive_palette:
                        for row in range(len(item.palette)):
                                for column in range(len(item.palette[row])):

                                        red_delta = abs(color.red - item.palette[row][column].red)
                                        green_delta = abs(color.green - item.palette[row][column].green)
                                        blue_delta = abs(color.blue - item.palette[row][column].blue)
                                        total_delta = red_delta + green_delta + blue_delta

                                        if approx_delta == 0:
                                                approximation.update(item.palette[row][column].name,item.palette[row][column].red,item.palette[row][column].green,item.palette[row][column].blue)

                                        elif total_delta < approximation["Total_Delta"]:
                                                approximation.update(item.palette[row][column].name,item.palette[row][column].red,item.palette[row][column].green,item.palette[row][column].blue)

                                        else:
                                                pass

                file.write("{0:s} can be duped with {1:s}\n".format(color.name, approximation.name))

print("This program has completed its operation without issue.")
