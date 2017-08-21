"""
Warframe Color Picker Program

Provide a RGB color code for a desired color and identify the closest
approximation of this color in the various color templates.

Command Line Syntax:
This script can be initiated by typing 'python3 ColorPicker.py'
(without the single quotes) into  the command line.

Associated Files:
Initialize.txt - Used to import the names of the various color template
files. If adding a new template file, simply add the name on a new line
in the file and update the number of lines indicated at the top of the
file.

Template Files - These files contain all of the RGB / Hex values for
the various color templates. These should not be modified. If adding a 
new file, follow the following convention:
    * The file should be a .txt file with no spaces in the title.
    * Each line should have the following values separated by commas
      and no spaces: column number, row number, red value, blue value,
      green value, hex value (e.g.-0x01A2B2)

Test_Input.txt - This file is used to indicate the colors that are
going to be compared to the templates. The following convention should
be followed when adding colors to the file:
    * Each color to be compared should be on a separate line.
    * Syntax for the color: Name,Hex Value (e.g.-0xFFBF00). There are
      no spaces after the comma.

Test_Output.txt - This file is created/updated with the name of the 
color template and the array location that is closest to the color
provided in the Test_Input.txt file.   
"""
class ColorCell:
    def __init__(self, name, red, green, blue):
        self.update(name, red, green, blue)

    def update(self, name, red, green, blue):
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

# Initialize major variables:
#    * List object "file_list" holds all the names of the standard Warframe pallettes.
#    * Dictionary object "archive_pallette" holds the representation of the Warframe pallettes.
#    * List object "test_colors" holds dictionaries of the colors to be tested.

file_list = []
archive_palette = []
test_colors = []

with open("Initialize.txt", "r") as file:
    file_size = int(file.readline().lstrip("Names =  ").rstrip("\n"))
    for line in range(file_size):
        file_list.append(file.readline().rstrip("\n"))

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
                        approx_delta = total_delta

                    elif approx_delta > total_delta:
                        approximation.update(item.palette[row][column].name,item.palette[row][column].red,item.palette[row][column].green,item.palette[row][column].blue)
                        approx_delta = total_delta

                    else:
                        pass

        file.write("{0:s} can be duped with {1:s}\n".format(color.name, approximation.name))

print("This program has completed its operation without issue.")
