from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from os import path
import urllib
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
htmlParser = "lxml"

# I used this website for searching and downloading pictures
# https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59

url_EP_members = r"https://www.europarl.europa.eu/meps/en/full-list/all"
html = urllib.request.urlopen(url_EP_members)
response = html.read()
soup = bs(response, htmlParser)
# Global variables
# Choose a small number so you can deal easily with all the info
n_members = 700  # Choose the number of members for which you would like to retrieve info
n_images = 2      # Number of Image you want to download per member
chromeOptions = Options()
#chromeOptions.headless = False
#chromeOptions.add_argument("--headless")'
fetch = r"erpl_image-frame mb-2"
fetch_name = 'alt'
fetch_src = 'style'
#//*[@id="i9"]/div[1]/span/div/div[1]/div[1]/c-wiz/div/a/div/div[1]/img
#//*[@id="i9"]/div[1]/span/div/div[1]/div[4]/c-wiz/div/a/div/div[1]/img
#//*[@id="i9"]/div[1]/span/div/div[1]/div[3]/c-wiz/div/a/div/div[1]/img
res=soup.find_all('div',attrs={'class': fetch}, partial = False)
names = [i.img[fetch_name] for i in res[:n_members]]
urls_background = [i.span[fetch_src] for i in res[:n_members]]

def scrap_img_url(url):
    text = url
    iterator = 0
    for elem in text:
        if (elem == '(' ):
            iterator2 = 0
            while(text[iterator + iterator2] != "'"):
                iterator2 += 1
            start = iterator + iterator2 + 1
            #print(start)
            #print(text[start])
            break
        iterator += 1
    iterator3 = -1 
    while (text[iterator3] != ")"):
        iterator3 -= 1
    end = iterator3 -1

    return text[start:end]

def replace_space_with_underscore(url): # This function is so that the image can be saved directly
    text = url
    iterator = 0
    for i in range(len(text)):
        if text[i] == ' ':
            break
    return text[:i] + '_' + text[i+1:]

def directory_exist(dire):
    
    if os.path.exists(dire):
        pass      
    else:
        os.mkdir(dire)

# Download images from the web
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(ChromeDriverManager().install(), options = chromeOptions)
#googl_img_url = 'https://www.google.be/imghp?hl=en&tab=ri&authuser=0&ogbl'

#driver.get(googl_img_url)
#xpath = '//*[@id="sbtc"]/div/div[2]/input'
#box = driver.find_element_by_xpath(xpath)

def set_browser():
    box.clear()

    
        

import time
def scroll_selenium():
    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
        
def find_images(n_images, name, dire):
    for i in range(1,n_images +1):
        try:
            print(os.getcwd())
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(dire + '/'+ name +str(i)+'.png')
        except:
            print('A little issue...')
            pass
#set_browser() 
def download_image_from_url(url, name, name2):
    #set_browser()
    response = requests.get(url)
    #print(os.getcwd())
    dire = os.getcwd() + '/folder_images/'
    directory_exist(dire)
    os.chdir(dire)
    #print(os.getcwd())  
    new_dir = os.getcwd() +'/' + name
    directory_exist(new_dir)
    print(new_dir + '/'+ name + '.jpeg')
    file = open(new_dir + '/'+ name + '.jpeg', "wb")
    file.write(response.content)
    file.close()
    #box.send_keys(name2)
    #box.send_keys(Keys.ENTER)
    #scroll_selenium()
    #find_images(n_images, name, new_dir)
    #box.clear()
    

    #print('Download of {}'.format(name))

    os.chdir(os.getcwd() + '/..')

    
            

names2 = [replace_space_with_underscore(i) for i in names[:n_members]]
url_img = [scrap_img_url(i) for i in urls_background[:n_members]]
##y = url_img[1]
##print(y)
##download_image_from_url(y,names2[1])
##response = requests.get(url_img[0])
##
##file = open("sample_image.png", "wb")
##file.write(response.content)
##file.close()

# Download the images from the website
for i in range(n_members):
    download_image_from_url(url_img[i], names2[i], names[i])
    #driver.quit()
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options = chromeOptions)
    googl_img_url = 'https://www.google.be/imghp?hl=en&tab=ri&authuser=0&ogbl'

    #driver.get(googl_img_url)
    xpath = '//*[@id="sbtc"]/div/div[2]/input'
    #box = driver.find_element_by_xpath(xpath)
    #driver.clear()
    #driver.close()
#driver.quit()

    #print(names2[i])






                      
#print (names)
#print (url_img)

