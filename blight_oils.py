import csv
import itertools
from distutils.util import strtobool

# Import Oils CSV to Dictionary 
with open('blight_oils.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    oil_dict = {}
    for row in reader:
        # row is list [Oil 1, Oil 2, Oil 3, Notable, Description]
        # oil_dict ('Oil 1', 'Oil 2', 'Oil 3') : ['Notable', 'Description']
        oil_dict[(row[0], row[1], row[2])] = row[3::]        

# Ensure positive integers only
def get_oil_count(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Whole numbers only please!")
            continue

        if value < 0:
            print("Positive numbers only!")
            continue
        else:
            break
    return value

# Get Yes or No
def yes_or_no(prompt):    
    while True:
        try:
            value = strtobool(input(prompt + "[y/n]: "))
        except ValueError:
            print("Yes or no please!")
            continue        
        else:
            break
    return value

# Define all 12 Oil Types for dict access in order of progression
clear = 'Clear Oil'	
sepia = 'Sepia Oil'
amber = 'Amber Oil'	
verdant = 'Verdant Oil'	
teal = 'Teal Oil'	
azure = 'Azure Oil'	
violet = 'Violet Oil'	
crimson = 'Crimson Oil'	
black = 'Black Oil'	
opal = 'Opalescent Oil'	
silver = 'Silver Oil'	
golden = 'Golden Oil'
	
# Prompt user for quantity of oils 
oil_count = {}
oil_count[clear] = get_oil_count("# of Clear Oils: ")
oil_count[sepia] = get_oil_count("# of Sepia Oils: ")
oil_count[amber] = get_oil_count("# of Amber Oils: ")
oil_count[verdant] = get_oil_count("# of Verdant Oils: ")
oil_count[teal] = get_oil_count("# of Teal Oils: ")
oil_count[azure] = get_oil_count("# of Azure Oils: ")
oil_count[violet] = get_oil_count("# of Violet Oils: ")
oil_count[crimson] = get_oil_count("# of Crimson Oils: ")
oil_count[black] = get_oil_count("# of Black Oils: ")
oil_count[opal] = get_oil_count("# of Opalescent Oils: ")
oil_count[silver] = get_oil_count("# of Silver Oils: ")
oil_count[golden] = get_oil_count("# of Golden Oils: ")
excess_flag = yes_or_no("Combine EXCESS oils? ")

# TODO Combine EXCESS Oils?
if excess_flag:
    excess = 0
    for k, v in oil_count.items():
        if excess > 0:
            v += excess
            excess = 0
        while v > 5:
            excess += 3
            v -= 3
        oil_count[k] = v
        excess //= 3

# Create iterator with a maximum of 3 of each Oil
oils_to_iterate = []
for key, value in oil_count.items():    
    if 0 < value <= 3:
        temp = [key] * value
        oils_to_iterate.extend(temp)

    # Maximum of 3 Oils in combination    
    if value > 3:
        temp = [key] * 3
        oils_to_iterate.extend(temp)

# Get Permutations of Oils, Order matters but only b/c data stored in dict
# ABC same as BCA in practice, but need to find it in dict
# Set avoids repeats, if x in oil_dict because key listed as ABC, not BCA. 
oil_permutations = set([x for x in itertools.permutations(oils_to_iterate, 3) if x in oil_dict])

# Display Results
for oils in oil_permutations:     
    print()
    print(oils[0] + ' + ' + oils[1] + ' + ' + oils[2])
    print(oil_dict[oils][0].upper())
    print(oil_dict[oils][1])
    print()
print("Results saved to results.csv")

# Save results to File
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    
    writer.writerow(["Oil Quantities"])
    writer.writerows(oil_count.items())
    writer.writerow([])

    for oils in oil_permutations:
        writer.writerow(oils)
        writer.writerow(oil_dict[oils])
        writer.writerow([])