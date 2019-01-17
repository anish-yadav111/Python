# Make sure you install PIL and BeautifulSoup
# to install run 
# 1. pip install Pillow
# 2. pip install BeautifulSoup

import sys
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup 


if len(sys.argv) == 1:
    search = input("What you want to search for ? ")
else:
    search =  " ".join(sys.argv[1:])

url = "https://www.bing.com/images/search?q={}".format(search)
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
aTag = soup.findAll("a",{"class":"thumb"})
result  = requests.get(aTag[1].attrs["href"])
try :
   img = Image.open(BytesIO(result.content))
   img.save("{}.{}".format(search,img.format))
   print("Successfully saved the image")
except:
    print("Error in saving the file")

