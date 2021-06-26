import ffmpeg
import vlc
from moviepy.editor import VideoFileClip
import speech_recognition as sr 
import math
class Video(VideoFileClip):
	def __init__(self, file_path, split_time = 15):
		super().__init__(file_path)
		self.split_time = split_time
		x = list(range(0,int(self.duration),self.split_time))
		x.append(math.ceil(self.duration) )
		self.cut_times = x


	def get_duration(self):
		return self.duration

	def get_split_time(self):
		return self.split_time

	def set_split_time(self, split):
		self.split_time = split
	
	def get_splits(self):
		return self.cut_times

	def set_splits(self):
		self.cut_times = list(range(0,int(self.duration),self.split_time))

		


		
	