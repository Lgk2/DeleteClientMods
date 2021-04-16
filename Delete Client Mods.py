import os
import glob


client_mods = []
with open('mods.txt') as file:
    for line in file:
        for word in line.split():
            client_mods.append(word)

count = 0

for cmodIndex in range(len(client_mods)):
    cmodString = client_mods[cmodIndex] + '*.jar'
    filesFound = glob.glob(cmodString)

    if len(filesFound) >= 1:
        os.remove(filesFound[0])
        print("Deleted " + cmodString)
        count += 1
    else:
        print("Did not find " + cmodString)
print("Tried to delete " + str(len(client_mods)) + " mods")
print("Finished deleting client mods. Deleted " + str(count) + " mods!")
