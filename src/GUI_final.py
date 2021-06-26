import PySimpleGUI as sg
import cv2
import os
import os.path as path
import base64
import numpy as np
import vlc
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig

# import python-vlc
from threading import  Thread
import threading
from sys import platform as PLATFORM
from personClass import Person
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
import PIL
#from threadClass import Thread
#from threading import  Thread
from transcriptionClass import Transcription
import math
import numpy as np
import os
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from scipy.io import wavfile
import librosa
import threading
from gtts import gTTS

from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer, Wav2Vec2Processor
import concurrent.futures
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer, Wav2Vec2Processor
import speech_recognition as sr
import torch
from matplotlib import pyplot as plt
#from videoClass import Video
#from threadClass import Thread

# Defining all the constants
CACHE_ = r'./cache/'
ASSET_ = r'./Assets/' 
AUDIO = './dre.mp3'
print('Make sure you change the directory before starting')
directory = r'c:/Users/astrid.tepie.zepe/Documents/ASIF_EP/src/'
os.chdir(directory)
ICON_ =  r'./logos/logo19.png'
LOGO_ = r'./logos/logo1.ico'
THEME_ = 'Dark Blue'

#Defining all the global variables
# INITIALIZATION

FILE = '../Video/test.mp4'
FRAME = cv2.imread(ICON_)
RET = 0
DURATION = 0
COPYRIGHT = "ASIF 2021 \u00a9"
NAME = ' '
NAMES = [ ]
IDs = [ ]
SUMMARY = "The summary will appear here.\n Please press summarize when the transcription is done."
TRANSCRIPTION = "The transcription will appear here.\n Please start the video and press transcribe."

# Initializing the video player
MEDIA = vlc.Media(FILE)
PLAYER = vlc.MediaPlayer()
PLAYER.set_media(MEDIA)

#Initializing the Audio Player
MEDIA_AUDIO = vlc.Media(AUDIO)
PLAYER_AUDIO = vlc.MediaPlayer()
PLAYER_AUDIO.set_media(MEDIA_AUDIO)

path = '../Meps'
Output = "../Summarizer/Output/"
images = []
classNames = []
myList = os.listdir(path)

# COMPUTER VISION

def upload_encoded_features(feature):
    encodeListMepsLoaded = np.load(feature, allow_pickle=True)
    return encodeListMepsLoaded


for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def update_name_list(liste, name):
    if (name in liste) or name is None or name == "Not a member":
            pass
    else:
        print("new name")
        liste.append(name)
        p = Person(int(name))
        NAMES.append(p.fullName)

def recognize(encoded_features='encodedMeps.npy'):
    while True:
        if sg.WIN_CLOSED:
            break
        encodeListMepsLoaded = upload_encoded_features(encoded_features)
        imgS = cv2.resize(FRAME, (0, 0), None, 0.50, 0.50)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListMepsLoaded, encodeFace)
            faceDist = face_recognition.face_distance(encodeListMepsLoaded, encodeFace)
            matchIndex = np.argmin(faceDist)
            
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                prob = str(faceDist[matchIndex])[:5]
                if faceDist[matchIndex] <= 0.5:
                    update_name_list(IDs, name)
                    window['-ATTENDEES-'].update(NAMES)
            else:
                name = "Not a member"
                update_name_list(IDs, name)
                window['-ATTENDEES-'].update(NAMES)
        time.sleep(1.5)
        if END:
            break
        

# SUMMARIZER

tokenizer=BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model=BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def text_summarize(text):

    # Encoding the inputs and passing them to model.generate()
    inputs = tokenizer.batch_encode_plus([text],return_tensors='pt')
    summary_ids = model.generate(inputs['input_ids'], early_stopping=True)

    # Decoding and printing the summary
    bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    # print(bart_summary)
    return bart_summary


# TEXT 2 SPEECH

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("summary.mp3")
    return

# GUI

def ImageButton(title, key, background = THEME_):
        return sg.Button(image_filename = title, button_color=(background, sg.theme_background_color()),
                    border_width=0, key=key)

def window():
    sg.theme('Dark blue')
    layoutMP3 = [
            ImageButton('./Assets/play_off.png', key='-PLAYAUDIO-'), 
            ImageButton('./Assets/pause_off.png', key='-PAUSEAUDIO-'), 
            ImageButton('./Assets/stop.png', key='-STOPAUDIO-'), sg.Text('     '),sg.Text(text = '00:00 / 00:00', key = '-MESSAGE_AREA_AUDIO-'), sg.Text,sg.Button('Summarize', key='-SUMMARIZE-', disabled = True, button_color = ('black','grey')),]

    layout3 = [
            [sg.Text("Summary")], 
            [sg.Multiline(SUMMARY ,enable_events=True, size=(40, 20), key='-SUMMARYTEXT-')],
            layoutMP3,]

    layoutMP4 = [
            [sg.Image(filename = ICON_, key='-IMAGE-')],
            [sg.Text(text = '          '), ImageButton('./Assets/play_off.png', key = '-PLAY-' ),  sg.Text(text = '                   '),
            ImageButton('./Assets/pause_off.png', key = '-PAUSE-' ),  sg.Text(text = '                     '),
            ImageButton('./Assets/stop.png', key = '-STOP-'),sg.Text('  ') ,sg.Text(text = '00:00 / 00:00', key = '-MESSAGE_AREA-',size = (12,1)),  ]]

    layout1 = [
        [sg.Text("File: "), sg.In(size=(25, 1), enable_events=True, key="-FILE-"), sg.FileBrowse(key = '-IN-'),], 
        [sg.Text("Attendee List"),],
        [sg.Listbox(NAMES, enable_events=True, size=(40, 5), key='-ATTENDEES-'),],
        [sg.Text("Transcription"),  ],
        [sg.Multiline(TRANSCRIPTION, enable_events=True, size=(40, 15), key = '-TRANSCRIPTIONTEXT-'),], 
        [sg.Button('transcribe', key='-TRANSCRIBE-'),] ]

    layout_final = [
        [   sg.Column(layout1),
            sg.VSeperator(),
            sg.Column(layoutMP4),
            sg.VSeperator(),
            sg.Column(layout3),] ]
    return  sg.Window('Demo Application -ASIF Summarizer', layout_final, location = (20, 20),  element_justification='center', finalize = True, resizable = True, icon = LOGO_)

# INITIALIZE OBJECTS 

window = window()    
p = Person()
transObject = Transcription(FILE)

# Initializing the video player
MEDIA = vlc.Media(FILE)
cap = cv2.VideoCapture(FILE)
PLAYER = vlc.MediaPlayer()
PLAYER.set_media(MEDIA)
PLAYER.set_hwnd(window['-IMAGE-'].Widget.winfo_id())

#Initializing the Audio Player
MEDIA_AUDIO = vlc.Media(AUDIO)
PLAYER_AUDIO = vlc.MediaPlayer()
PLAYER_AUDIO.set_media(MEDIA_AUDIO)


def do():   
    transObject.write_mp3()
    transObject.create_audio_cuts()
    transObject.create_threads()

#Initializing and starting threads for face recognition and speech to text  
start_thread = Thread(target = do)       # speech to text
start_thread.start()

thread_face = Thread(target = recognize) # face recognition
thread_face.start()

TRANS = False
SUMMA = False
TRANSDONE = False
END = False
# MAIN THREAD 
while True :
    event, values = window.read(timeout = 20)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        PLAYER.stop()
        PLAYER_AUDIO.stop()
        END = True
        quit()
        break
    ## VIDEO 
    elif event == '-PLAY-':
        
        PLAYER.play()
        time.sleep(0.2)                 # Timeout needed, to extract info after the media starts to play
        DURATION = MEDIA.get_duration()
        RECORDING = True
        pass
    elif event == '-PAUSE-':
        PLAYER.pause()
        RECORDING = False
        pass
    elif event == '-STOP-':
        PLAYER.stop()
        window['-IMAGE-'].update(ICON_)
        PLAYER.set_time(0)
        RECORDING = False

        pass

    ## AUDIO
    elif event == '-PLAYAUDIO-':
        PLAYER_AUDIO.play()
        time.sleep(0.2)                 # Timeout needed, to extract info after the media starts to play
        DURATION_AUDIO = MEDIA_AUDIO.get_duration()

    elif event == '-PAUSEAUDIO-':
        PLAYER_AUDIO.pause()
        
    elif event == '-STOPAUDIO-':
        PLAYER_AUDIO.stop()
        PLAYER_AUDIO.set_time(0)

    ## TRANSCRIPTION
    elif event == '-TRANSCRIBE-':
        sg.Popup('Transcription is about to begin, all cache data will be removed', keep_on_top=True)
        #os.remove(transObject.mp3_path)
        transObject.activate_threads2()
        transObject.transcription_flag = True

        TRANS = True
        
        window['-TRANSCRIBE-'].update(disabled = True, button_color = ('black','grey') )

    if start_thread.isAlive():
        window['-TRANSCRIBE-'].update(disabled = True, button_color = ('black','grey') )
    elif not start_thread.isAlive() and TRANS == False:
        window['-TRANSCRIBE-'].update(disabled = False, button_color=('black', sg.theme_background_color()) )
  
    if not start_thread.isAlive() and TRANS == True:  # The thread creating the transcription threads is done

        if transObject.transcription_flag :
            print("Transcribing")
            window['-TRANSCRIBE-'].update(disabled = True, button_color = ('black','grey') )
            TRANSCRIPTION = f"Loading ... {int(transObject.check_progress()/(transObject.n_cuts - 1)*100)} %"
            window['-TRANSCRIPTIONTEXT-'].update(TRANSCRIPTION)

        if transObject.check_progress() == transObject.n_cuts - 1 :
            print("The transcription is done")
            transObject.generate_transcript()
            TRANSCRIPTION = transObject.final_transcription
            window['-TRANSCRIPTIONTEXT-'].update(TRANSCRIPTION)
            window['-TRANSCRIBE-'].update(disabled = False, button_color=('black', sg.theme_background_color()))
            transObject.transcription_flag = False
            TRANS = False
            
            window['-SUMMARIZE-'].update(disabled = False, button_color=('black', sg.theme_background_color()))
            TRANSDONE = True


    ## SUMMARY
    elif event == '-SUMMARIZE-' and TRANSDONE:
        TRANSDONE = False
        window['-SUMMARIZE-'].update(disabled = True, button_color = ('black','grey') )
        SUMMARY = text_summarize(TRANSCRIPTION)
    
        #SUMMARY = "No summary to show..."
        window['-SUMMARYTEXT-'].update(SUMMARY)
        text_to_speech(SUMMARY)
        #window['-SUMMARIZE-'].update(disabled = False, button_color=('black', sg.theme_background_color()))
        AUDIO = "summary.mp3"
        MEDIA_AUDIO = vlc.Media(AUDIO)
        PLAYER_AUDIO.set_media(MEDIA_AUDIO)
    
    ## PROCESSING FILES
    elif event == '-FILE-':
        PLAYTIME = PLAYER.get_time()
        PLAYER.stop()
        FILE = values["-FILE-"]
        try: # Updating all the fields
            MEDIA = vlc.Media(FILE)
            cap = cv2.VideoCapture(FILE)
            transObject = Transcription(FILE)
            
            start_thread = Thread(target = do)
            start_thread.start()
            window['-TRANSCRIPTIONTEXT-'].update("The transcription will appear here.\n Please start the video and press transcribe.")
            SUMMARY = "The summary will appear here.\n Please press summarize when the transcription is done."
            window['-SUMMARYTEXT-'].update(SUMMARY)

            PLAYER.set_media(MEDIA)
            window['-IMAGE-'].update(ICON_)  
            sg.Popup('You are changing videos, all cache data will be removed', keep_on_top=True)
            NAMES = [ ]
            window['-ATTENDEES-'].update(NAMES)
        except:
            PLAYER.set_time(PLAYTIME)
            pass


    if (PLAYER_AUDIO.is_playing()):
        window['-MESSAGE_AREA_AUDIO-'].update("{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(PLAYER_AUDIO.get_time()//1000, 60), *divmod(DURATION_AUDIO//1000, 60)))

    
    if (PLAYER.is_playing()):
        ret, FRAME = cap.read()
        window['-MESSAGE_AREA-'].update("{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(PLAYER.get_time()//1000, 60), *divmod(DURATION//1000, 60)))
        if(PLAYER.get_time() == DURATION):
            print(MEDIA.get_duration())
            print("The video has stopped")
            window['-IMAGE-'].update(ICON_)
    else:
        pass

    if  not thread_face.is_alive() :
        print("Thread is starting")
        thread_face = Thread(target = recognize)
        thread_face.start()


    


        






