print('Hello plz make sure the following libraries are installed')
print('>>> google-api-python-client')
print('>>> urllib')
print('>>> pafy')
import time

print('Are the required libraries installed?')
x = input('[Y/N]')

if str(x) == 'Y' or str(x) =='y':
    print("Let's proceed")
else:
    print('plz avoid wasting time and install the necessary libraries')
    print('1', end = '')
    time.sleep(1)

    print('2', end = '')
    time.sleep(1)

    print('3', end = '')
    time.sleep(1)

    print('.', end = '')
    time.sleep(1)

    print('.', end = '')
    time.sleep(1)

    print('.', end = '')
    time.sleep(1)
    
    time.sleep(1)
    count = 0
    z = str(input('Are you done? [Y/N]'))
    zz = z != 'Y' and z != 'y'

    while( zz ):
        if count == 0:
            print("Get busy")
        else:
            t = 0
        z = str(input('Are you done? [Y/N]'))
        zz = z != 'Y' and z != 'y'
        print(zz)
         
        count +=1
    print("Let's proceed")
   
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import os
import os.path as path
import  pafy

##################################################################################
##################################################################################
####################### GET THE PLAYLIST##########################################
##################################################################################
##################################################################################


#extract playlist id from url
print('Do you wish to use your own playlist?')
y = input('[Y/N]')
if y == 'Y' or y == 'yes':
    print("Let's have a look at your music taste...")
    time.sleep(2)
    print('plz paste in the youtube URL, to get the correct URL go to your playlist and click on share...')
    url = str(input('Youtube URL : '))
else:
    print('European parliament playlist used...')
    url = 'https://youtube.com/playlist?list=PLHQxK2YVsFVvtXs3P_W_7FEttbCzRqjmq'  # URL of youtube playlist





query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]

print(f'get all playlist items links from {playlist_id}')
# This is an API, you have to install the google API from pip install google-api-python=client
# May be other ways to do so?
#You have to enable the youtube API from google
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyCBz5v1nSJmcFb_yHMOGlH3k-PZIU2Yq28")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 50
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

print(f"total: {len(playlist_items)}")
links = []
for t in playlist_items:
    links.append(f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s')

print(links)


##################################################################################
##################################################################################
####################### DOWNLOAD VIDEO ###########################################
##################################################################################
##################################################################################

# Download the Pluralsight 'we are one' video
# url of video


def download_vid(url,download_videos = '/download_folder'):
    cwd = os.getcwd() # Get the current working directory
    download_videos = cwd + download_videos
    if (path.exists(download_videos)): # Check if the download_videos folder exists, if not then it is created
        print(f'path {download_vid} already exists')
    else:
        os.mkdir(download_videos)
        
    #os.chdir(download_videos )
        
    # create video object
    video = pafy.new(url)
    # extract information about best resolution video available 
    bestResolutionVideo = video.getbest()
    # download the video
    bestResolutionVideo.download(download_videos)
    #os.chdir('/..') # Go backward in the directory

if __name__ == '__main__':# This command executes the code if this file is executed (run - f5)
    t = 1
    for link in links:
        print(f'Downlaod {t}/{len(links)}')
        download_vid(link) # you can specify the directory where you want to store the videos
        t +=1






