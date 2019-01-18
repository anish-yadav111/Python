# Make sure you install PIL and BeautifulSoup
# to install run 
# 1. pip install Pillow
# 2. pip install BeautifulSoup

import sys
import pymongo
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


if len(sys.argv) == 1:
    search = input("What you want to search for ? ")
else:
    search =  " ".join(sys.argv[1:])

url = "https://in.images.search.yahoo.com/search/images;?p={}".format(search)
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
images_array = soup.find_all("img",{"class":"process"})
result  = requests.get(images_array[0].attrs["data-src"])
try :
   img = Image.open(BytesIO(result.content))
   img.save("{}.{}".format(search,img.format))
   print("Successfully saved the image")
except:
    print("Error in saving the file")

