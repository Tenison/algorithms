##simple linear search algorithm
## find number 

FIND_NUMBER  = 4

list_of_numbers = [12, 13, 15, 4, 0, 9, 99]

found = False
count = 0

for number in list_of_numbers :
    if number == FIND_NUMBER :
        found = True
        count += 1
if found :
    print(f"Found {FIND_NUMBER} in the list")
else : 
    print(f"{FIND_NUMBER} was not found in the list")


