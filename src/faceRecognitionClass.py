import face_recognition
import classPerson
import cv2
import os 
from os import path
class Recognition( ):

	def __init__(self, dataset, encoded, path):
		self.dataset = dataset
		self.person = None
		
		self.encoded = encoded
		self.IDs = None


	def findEncodings(self, images):
	    encodeList = []
	    for img in images:
	        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	        encode = face_recognition.face_encodings(img)[0]
	        encodeList.append(encode)
	    return encodeList




	def encode_dataset(self,dataset_path):
		images = []
		classNames = []
		myList = os.listdir(dataset_path)

		for cl in myList:
		    curImg = cv2.imread(f'{path}/{cl}')
		    images.append(curImg)
		    classNames.append(os.path.splitext(cl)[0])
		set_IDs(classNames)
		return findEncodings(images)

	def set_encoded_dataset(self, encodings):
		self.encoded = encodings

	def get_enocoded_dataset(self):
		return self.encoded

	def set_IDs(self, ID):
		self.IDs = ID

	def get_IDs(self):
		return self.IDs

	def get_face_encoding_person(self, person):
		matches = face_recognition.compare_faces(encodeListMepsLoaded, encodeFace)
		faceDist = face_recognition.face_distance(encodeListMepsLoaded, encodeFace)
		matchIndex = np.argmin(faceDist)
		idx = self.get_IDs()
		return idx(matchIndex)

	def get_person_info(person):
		# This function will return the name and info of the person
		p = Person(person)
		
		return p

	def set_person_info(self):
		# To define when the function, encode new feature will be implemented
		pass





	def set_person(self, person):
		self.person = person

	def get_person(self):
		return self.person

	def compare_with_current_person(new_person, current_person):
		matches = face_recognition.compare_faces(new_person, current_person)
		faceDist = face_recognition.face_distance(new_person, current_person)
		var = True
		if faceDist < 0.5:
			var = True
		else:
			var = False
		return var





