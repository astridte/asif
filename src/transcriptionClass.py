import speech_recognition as sr
#from speech_recognition import Recognizer as r
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from videoClass import Video
from threadClass import Thread
import os 
r = sr.Recognizer()


def concatenate_sentence(res):
		x = ' '
		y = ' '
		for elem in res:
			x = x  + elem + y

		return x


class Transcription():
	def __init__(self, video_path = r'../Video/test.mp4', type = "google", mp3_path = r'./cache/'):
		self.final_transcription = None
		self.intermediate_transcription = ' '
		self.type = type
		self.video = Video(video_path)
		self.duration = self.video.get_duration()
		self.audio = self.video.audio
		self.cuts = self.video.cut_times
		self.n_cuts = len(self.cuts)
		self.mp3_path = mp3_path
		self.transcript_threads = [0]*(self.n_cuts - 1)
		self.transcription_flag = False


	def update(self):
		self.final_transcription = None
		self.intermediate_transcription = ' '
		self.duration = self.video.get_duration()
		self.audio = self.video.audio
		self.cuts = self.video.cut_times
		self.n_cuts = len(self.cuts)
		self.transcript_threads = [0]*(self.n_cuts - 1)
		self.transcription_flag = False

	


	def generate_transcript(self):
		# self.update()
		# self.set_flag()
		#self.write_mp3()
		# self.create_audio_cuts()
		# self.create_threads()
		# self.activate_threads2()
		# print(len(self.transcript_threads))
		# while self.check_progress() != self.n_cuts - 1:
		# 	pass
			
		print("Done")
		x = ' '
		y = ' '
		for elem in self.transcript_threads:
			x = x + elem.get_result() + y

		result = [elem.get_result() for elem in self.transcript_threads]
		result = concatenate_sentence(result)
		self.final_transcription = x
		self.clear_flag()


	
	def get_flag(self):
		return self.transcription_flag

	def set_final(self, setf):
		self.final_transcription = setf

	def get_final(self):
		return self.final_transcription

	def set_intermediate(self, seti):
		self.intermediate_transcription = seti

	def get_intermediate(self):
		return self.intermediate_transcription

	# def concatenate(self, concat = []):
	# 	try:
	# 		x = self.get_intermediate + ' '
	# 		for elem in concat:
	# 			x = x + ' ' + elem
	# 	except:
	# 		x = None
	# 	return self.set_intermediate(x)
	def transcribe(self, audio, type = "google"):
		if type.lower() == "google":
			audioclip = sr.AudioFile(audio)
			with audioclip as source: 
				audio_file = r.record(source)
			transcription = r.recognize_google(audio_file)
			return transcription

		elif type.lower() == "wav2vec":
			pass
		elif type.lower() == "speech2text":
			pass
	def set_flag(self):
		self.transcription_flag = True
	def clear_flag(self):
		self.transcription_flag = False

	def write_mp3(self ):
		if os.path.isdir(self.mp3_path):
			pass
		else:
			os.mkdir(self.mp3_path)
		self.mp3_file = self.mp3_path + '/audio.wav'
		self.audio.write_audiofile(self.mp3_file)

	def create_audio_cuts(self):
		for i in range(self.n_cuts-1):
			ffmpeg_extract_subclip(self.mp3_file, self.cuts[i], self.cuts[i+1], targetname = self.mp3_path + f"cut{i}.wav" )

	def create_threads(self):
		ls = [ ]
		for i in range(self.n_cuts-1):
			t = Thread(self.transcribe , args = (self.mp3_path + f"cut{i}.wav",))
			#print(self.mp3_path + f"cut{i}.wav",)
			ls.append(t)
		self.transcript_threads = ls
		print("threads are created")

	def get_transcript_threads(self):
		#self.create_threads()
		return self.transcript_threads

	def activate_threads2(self, threads_in_parallel = 3):
		for elem in self.transcript_threads:
			elem.start()
		print("Threads is started")

	def check_progress(self):
		self.transcript_threads
		ls = [not elem.isAlive() for elem in self.transcript_threads]
		return sum (ls)



	def activate_threads(self, threads_in_parallel = 3):
		self.set_flag()
		n = self.n_cuts
		x = 0 
		y = x + threads_in_parallel
		steps = n // threads_in_parallel
		step = 0 
		while (step <= steps ):	
			for i in range(x,y):
				self.transcript_threads[i].start()
			x = y
			y += threads_in_parallel

			if y >= n:
				y = n	
			while self.transcript_threads[i].is_alive():
				pass
	def get_status(self):
		return self.check_progress()/self.n_cuts

	# def final_step(self):
	# 	set_flag()
	# 	liste = self.transcript_threads
	# 	res = [ ]
	# 	for elem in liste:
	# 		res.append(elem.get_results())
	# 	x = self.concatenate(res)
	# 	set_final(x)
	# 	clear_flag()




	


