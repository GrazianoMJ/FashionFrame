# Warframe Color Picker Program
# Written by: Mike Graziano
# Version: 1.1

class ColorCell:
        def __init__(self,red,green,blue):
                self.red = red
                self.green = green
                self.blue = blue
                self.hex = red*(16**4)+green*(16**2)+blue
                self.RGBtext = "({0:d},{1:d},{2:d})".format(red,green,blue)
                self.HEXtext = "0x{0:X}".format(self.hex)

        def update(self,red,green,blue):
                self.red = red
                self.green = green
                self.blue = blue
                self.hex = red*(16**4)+green*(16**2)+blue
                self.RGBtext = "({0:d},{1:d},{2:d})".format(red,green,blue)
                self.HEXtext = "0x{0:X}".format(self.hex)

class ColorPalette:
        def __init__(self, name):
                self.name = name
                self.palette = [[ColorCell(0,0,0) for y in range(5)] for x in range(18)]

""" Initialize major variables:
        * List object "file_list" holds all the names of the standard Warframe pallettes.
        * Dictionary object "archive_pallette" holds the Python representation of the Warframe pallettes.
        * List object "test_colors" holds dictionaries of the colors to be tested. """
file_list = []
with open("Initialize.txt", "r") as file:
        file_size = int(file.readline().lstrip("Names =  ").rstrip("\n"))
        for line in range(file_size):
                file_list.append(file.readline().rstrip("\n"))
archive_pallette = {}
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
                                file_palette.palette[row][column].update(line_buffer[2],line_buffer[3],line_buffer[4])

        archive_pallette.update({item: file_palette})

"""# Create test colors list from "Test_Input.txt" file
with open("Test_Input.txt", "r") as file:
    for line in file:
        line_buffer = line.rstrip().split(",")
        test_colors.append({
            "Name": line_buffer[0],
            "Red": int(line_buffer[1][0:4], 0),
            "Green": int(line_buffer[1][0:2] + line_buffer[1][4:6], 0),
            "Blue": int(line_buffer[1][0:2] + line_buffer[1][6:8], 0),
            "HEX": line_buffer[1]
        })

# Determine the best approximation for each color and output it to the "Test_Output.txt" file
with open("Test_Output.txt", "w") as file:
    for color in test_colors:
        approximation = dict.fromkeys(["Pallette", "Column", "Row", "Red", "Green", "Blue", "HEX", "Total_Delta"])
        for item in file_list:
            for column in range(len(archive_pallette[item])):
                for row in range(len(archive_pallette[item][column])):

                    red_delta = abs(color["Red"] - archive_pallette[item][column][row]["Red"])
                    green_delta = abs(color["Green"] - archive_pallette[item][column][row]["Green"])
                    blue_delta = abs(color["Blue"] - archive_pallette[item][column][row]["Blue"])
                    total_delta = red_delta + green_delta + blue_delta

                    if approximation["Total_Delta"] is None:
                        approximation = {
                            "Pallette": item,
                            "Column": column,
                            "Row": row,
                            "Red": archive_pallette[item][column][row]["Red"],
                            "Green": archive_pallette[item][column][row]["Green"],
                            "Blue": archive_pallette[item][column][row]["Blue"],
                            "HEX": archive_pallette[item][column][row]["HEX"],
                            "Total_Delta": total_delta
                        }
                    else:
                        if total_delta < approximation["Total_Delta"]:
                            approximation = {
                                "Pallette": item,
                                "Column": column,
                                "Row": row,
                                "Red": archive_pallette[item][column][row]["Red"],
                                "Green": archive_pallette[item][column][row]["Green"],
                                "Blue": archive_pallette[item][column][row]["Blue"],
                                "HEX": archive_pallette[item][column][row]["HEX"],
                                "Total_Delta": total_delta
                            }

        file.write("{0:s} can be duped with {1:s} ({2:d},{3:d})\n".format(
            color["Name"], approximation["Pallette"], approximation["Column"]+1, approximation["Row"]+1
        ))"""

print("This program has completed its operation without issue.")
