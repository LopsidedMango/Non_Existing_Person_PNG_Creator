import bs4
import requests
from PIL import Image
from io import BytesIO
import time
# 110 seconds to do 50
size = int(input("How many photos do you want?"))
print("That will be about", str(round((1.12*size), 2)), "MB, estimated time about:", (size // 60), "minutes and", (size % 60), "seconds")
main_location = str(input("Input main file location e.g C:\\Users\\*NAME*"))
print("Starting Now")

for i in range(0, size):
    url = "https://thispersondoesnotexist.com/image"
    if main_location == "":
        main_location = "C:\\Users\\22MatsonT636\\OneDrive - The College of Richard Collyer\\Computer Science\\Projects\\Car Park\\Data\\people_photos\\"
    file_name = "people_photo"
    number = str(i)
    formatter = ".png"
    actual = main_location.strip() + file_name.strip() + number.strip() + formatter.strip()
    img_binary = requests.get(url).content
    img = Image.open(BytesIO(img_binary))
    
    img.save(actual)
    time.sleep(0.2)
    print((i+1), "completed", (size-(i+1)), "to go")
print("Done")