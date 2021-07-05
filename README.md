# ASIF Meeting Minute Summarizer

## Description of the project

This project is a partial fulfilment of the Intelligent Interface course of Post-graduate program in Artificial Intelligence of Erasmus Hogeschool Brussel. The project is a 
 meeting minute summarizer used on videos of the daily ;eetings in the European Parliament. The summarizer does the following tasks:
 
 * Recognizes the member of the European Parliament
 * Transcribes spoken words to text 
 * Summarizes transcribed text
 * And reads out loud the summarized text

This project is built as a UI which loads video meetings and does the job. 
At the current state, the project is only tested in a one person meeting, further developement has to be made to adapt summarization to multiple people interacting with each other.

## Installation of dependencies
Installation of Visual Studio C++ is needed for dlib
https://visualstudio.microsoft.com/downloads/
Visual Studio Build tools 2019
C++ build tools

Installation of cmake is required
https://cmake.org/download/

Installation of vlc media player
https://vlc-media-player.en.uptodown.com/windows

### Requirement
This code has been tested on windows 10, with python 3.7 and all the package requirements can be found in the requirement.txt file. 

## How to install the project?

### Step 1 : Download the project or clone the repository
The first step of this project is to download the repository or clone the repository on your local repository. 
![alt text](https://github.com/astridte/asif/blob/main/step1.PNG)

### Step 2 : Create a python virtual environment
* Create a virtual environment  $ python -m venv venv

![alt text]( https://github.com/astridte/asif/blob/main/venv2.PNG )

* Activate the virtual environment $ .\venv\Scripts\activate

![alt text]( https://github.com/astridte/asif/blob/main/venv.PNG )

* install the requirement.txt file $ pip install -r .\path\to\requirement.txt

### Step 3 : Run the project
In order to run the project you have to run the GUI_final.py file that is found in the src folder.

## How to use the UI
The UI is very easy to use, it consists:
* A video media player (face recognition is automatic)
* A transcriber 
* A summarizer
* An audio media player


## Sources 
Some sources for this project can be listed here
* https://github.com/ageitgey/face_recognition
* https://pypi.org/project/gTTS/
* https://arxiv.org/abs/1810.04805
* https://www.europarl.europa.eu/portal/en


