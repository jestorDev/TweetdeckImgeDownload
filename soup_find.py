from bs4 import BeautifulSoup
import os
import time
import random

import urllib.request

soup= BeautifulSoup(open("TweetDeck.html"))

tags =  soup.findAll("a", {"rel" : "mediaPreview"})

linkss= set()

for tag in tags : 
    print(len(tags), " ---------------------------------")

    if tag.attrs['style'] :
        background = str ( tag.attrs['style'])
        str_background = background [21: background.find('?')]

        if "pbs.twimg.com/media/" in str_background :
            linkss.add(str_background)

        print(str_background)

folder = time.strftime("%Y-%m-%d")

os.makedirs( "./"+ time.strftime("%Y-%m-%d"), exist_ok=True)


downloaded = set ()

with open("dowloaded.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        downloaded.add(line.strip())


with open("dowloaded.txt",'a+',encoding = 'utf-8') as f:

    for link in linkss :
        file_name =link.split("/")[-1]
        file  = "./" + folder + "/"+ file_name
        #print( "File : ",file, " Link: ", link)
        
        if   file_name not in downloaded:
            f.write( file_name + "\n")
            urllib.request.urlretrieve( link, file)
            seconds =sorted((0.2, random.gauss(0.5 , 0.5), 0.7))[1]
            time.sleep(seconds)
            
