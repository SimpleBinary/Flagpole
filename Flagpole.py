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
    else:
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
                "Armenia": image("Armenia"),
                "Artsakh": image("Artsakh"),
                "Australia": image("Australia"),
                "Austria": image("Austria"),
                "Azerbaijan": image("Azerbaijan"),
                "Bahamas": image("Bahamas"),
                "Bahrain": image("Bahrain"),
                "Bangladesh": image("Bangladesh"),
                "Barbados": image("Barbados"),
                "Belarus": image("Belarus"),
                "Belgium": image("Belgium"),
                "Belize": image("Belize"),
                "Benin": image("Benin"),
                "Bhutan": image("Bhutan"),
                "Bolivia": image("Bolivia"),
                "Bosnia and Herzegovina": image("Bosnia and Herzegovina"),
                "Botswana": image("Botswana"),
                "Brazil": image("Brazil"),
                "Brunei": image("Brunei"),
                "Bulgaria": image("Bulgaria"),
                "Burkina Faso": image("Burkina Faso"),
                "Burundi": image("Burundi"),
                "Cambodia": image("Cambodia"),
                "Cameroon": image("Cameroon"),
            }

print("Calculating...")
print("Looks Like: " + min(countries, key=countries.get))
print("Similarity:", countries[min(countries, key=countries.get)][0], "(where 0 is identical)")
input()
