
import requests
from PIL import Image
from io import BytesIO
import time
import os
# 110 seconds to do 50
size = int(input("How many photos do you want?"))


main_location = str(input("Input main file location e.g C:\\Users\\*NAME*"))
max_file_size = int(input("What do you want your maximum file size to be? [in bytes]"))
if max_file_size == 0:
    max_file_size = 5500
print("That will be about", str(round((max_file_size*size), 2)), "Bytes, estimated time about:", (size // 60), "minutes and", (size % 60), "seconds")
print("Starting Now")
x = 0 
for i in range(0, size):
    
    url = "https://thispersondoesnotexist.com/image"
    time.sleep(1)
    if main_location == "":
        main_location = "C:\\Users\\"
    file_name = "people_photo"
    number = str(x)
    formatter = ".jfif"
    actual = main_location.strip() + file_name.strip() + number.strip() + formatter.strip()
    img_binary = requests.get(url).content
    
    img = Image.open(BytesIO(img_binary))
    
    img = img.resize((145, 180))
    
    img.save(actual)
    file_size = os.path.getsize(actual)
    
    if file_size > max_file_size:
        x-= 1
        

    
    
    print((x+1), "completed", (size-(x+1)), "to go")
    x+= 1
print("Done")
