import subprocess

from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from os import path
import urllib
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
import pathlib
import cv2 as cv
import dlib

htmlParser = "lxml"

def replace_space_with_underscore(url): # This function is so that the image can be saved directly
    text = url
    iterator = 0
    for i in range(len(text)):
        if text[i] == ' ':
            break
    return text[:i] + '_' + text[i+1:]

# I used this website for searching and downloading pictures
# https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59

url_EP_members = r"https://www.europarl.europa.eu/meps/en/full-list/all"
html = urllib.request.urlopen(url_EP_members)
response = html.read()
soup = bs(response, htmlParser)
# Global variables
# Choose a small number so you can deal easily with all the info
n_members = 3   # Choose the number of members for which you would like to retrieve info
n_images = 3      # Number of Image you want to download per member
chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument("--headless")
fetch = r"erpl_image-frame mb-2"
fetch_name = 'alt'
fetch_src = 'style'
#//*[@id="i9"]/div[1]/span/div/div[1]/div[1]/c-wiz/div/a/div/div[1]/img
#//*[@id="i9"]/div[1]/span/div/div[1]/div[4]/c-wiz/div/a/div/div[1]/img
#//*[@id="i9"]/div[1]/span/div/div[1]/div[3]/c-wiz/div/a/div/div[1]/img
res=soup.find_all('div',attrs={'class': fetch}, partial = False)
names = [i.img[fetch_name] for i in res[:n_members]]
names2 = [replace_space_with_underscore(i) for i in names[:n_members]]
urls_background = [i.span[fetch_src] for i in res[:n_members]]

path = os.getcwd() + '/dataset/'
hog_face_detector =  dlib.cnn_face_detection_model_v1('./mmod_human_face_detector.dat')
#dlib.get_frontal_face_detector()
def rename_files_dataset(pathn, name):
    directories = os.listdir(pathn)
    for j in range(len(directories)):
        dire = directories[j]
        add = '000'

        if j < 10:
            add = add[:2]+str(j)
        elif j > 9 and j < 100:
            add = add[:1] + str(j)
        else:
            add = str(j)
        os.rename(pathn + '/' + dire, path + '/' + name + '/' + name + add + '.jpeg')
            
        


for i in range(len(names2)):
    name = names2[i]
    path_member = path + name
    print(f"[INFO]Download of file for {name} has started")
    print(f"[INFO]{i + 1}/{n_members}")  
    a = subprocess.run(["idt","run","-i",name,"-s",str(n_images)])
    #a.terminate()
    print(f"[INFO]Proceeding with some data cleaning ")
    print(f"[INFO]Deleting some pictures")
    counter = 0
    rename_files_dataset(path_member, name)
    all_pictures = os.listdir(path_member)

    for j in range(len(all_pictures)):
        delete = []
        picture_path = path_member + '/' + all_pictures[i]
        image = cv.imread(picture_path)
        face = hog_face_detector(image,2)
        number_face = len(face)
        if number_face != 1:
            counter += 1
            delete.append(j)
            

        else:
            pass
        
    for elem in delete:        
        os.remove(path_member + '/' + all_pictures[elem])

    rename_files_dataset(path_member, name)
    counter = len(delete)



    print(f"[INFO]Out of {len(all_pictures)}, { n_images-counter} are left and {counter } were deleted")

        

             
        
        
    
    
