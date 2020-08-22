# Guided Exploration No. 3
# ALEX CASTRILLO

# This imports the random library to this file
import random

# This collects all possible names
possible_names = []

# The line below opens a file named rap-names-output.txt and collect all the rap names created by the program
outputFile = open('rap-names-output.txt', 'w')

# This line opens the rap-names.txt file as a read only file to pull the rap name info to be used and referred to as dataFile
with open('rap-names.txt', 'r') as dataFile:
    # for loop for the rap-names.txt file to go through each line in the file
    for name in dataFile:
        # each iteration of the file removes the space to have the names be next to each other and added to possible_names
        possible_names.append(name.rstrip())
        # The line below asks the user how many rap names they would like
count = int(input('How many rap names would you like to create? '))
# The line below asks the user how many parts the rap name should have
parts = int(input('How many parts should the name contain? '))

# the line below runs a for loop following the amount that the user requested
for i in range(count):
    # line below is an accumulator for the names generated
    name_parts = []
    # the line below is a for loop for how many parts of the name the user wants
    for j in range(parts):
        # the line below adds a name per loop to the name_parts list.
        name_parts.append(possible_names[random.randint(0, len(possible_names) - 1)])

    # The line below will take the generated names and list it to the file opened earlier(rap-names-output.txt) separating each part of the name with a space and a line below
    outputFile.write(f"{' '.join(name_parts)}\n")
# The line below prints out each generated names into the python preview
    print(f"{' '.join(name_parts)}")
# The line below closes the file opened in line 11
outputFile.close()
