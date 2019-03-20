from PIL import Image
from sys import platform
import imagehash

print("Flagpole")
userFlagDir = str(input("Enter the directory that stores your flags > "))
userInput = str(input("Enter the path to the flag you want to test > "))
try:
    userHash = imagehash.average_hash(Image.open(userInput))
except:
    print("Invalid File - Must be a local file path")
    exit()

def image(x):
    if platform.lower() == "win32":
        return userHash - imagehash.average_hash(Image.open(userFlagDir + "\\" + x + ".png")),
    else
        return userHash - imagehash.average_hash(Image.open(userFlagDir + "/" + x + ".png")),

countries = {
                "Abkhazia": image("Abkhazia"),
                "Afghanistan": image("Afghanistan"),
                "Albania": image("Albania"),
                "Algeria": image("Algeria"),
                "Andorra": image("Andorra"),
                "Angola": image("Angola"),
                "Antigua and Barbuda": image("Antigua and Barbuda"),
                "Argentina": image("Argentina"),

            }

print("Calculating...")
print("Looks Like: " + min(countries, key=countries.get))
print("Similarity: " + str(countries[min(countries, key=countries.get)]))
input()
