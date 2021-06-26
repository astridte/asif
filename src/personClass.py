import pandas as pd

class Person():
	def __init__(self, ID = 204335, mep_file_path = 'dataset.xlsx'):
		
		#get_mep_file(mep_file_path) 
		dataset = pd.read_excel(mep_file_path)
		try:

			index = dataset.set_index('id').index.get_loc(ID)
			fun1 = dataset.iloc[index][ 'politicalGroup'] + ', and '
			fun2 = dataset.iloc[index]['nationalPoliticalGroup']
			country = dataset.iloc[index]['country'] 
			full = dataset.iloc[index]['fullName']
		except:
			index = None
			ID = None
			dataset = None
			fun1 = fun2 = 0
			full = None
			country = None
		

		self.ID = ID
		self.dataset = dataset
		self.index = index
		self.functions = fun1 + fun2 
		self.fullName = full
		# self.firstName = get_firstName_db()
		# self.lastName = get_lastName_db()
		self.country = country
		self.intruder = False
		# self.encoded_mep_file = None

	def get_mep_file(mep_file_path):
		try:
			dataset = pd.read_excel(mep_file_path)
		except Exception:
			print(">>> Your dataset does not exist in your local directory.")
			dataset = None

		self.dataset = dataset
		return dataset


	#########################################################
	####      Defining the Getters and the Setters     ######
	#########################################################

	def get_index(self):          # Corresponding index in the db file
		return self.index

	def set_index(self, idx):
		self.index = idx

	def get_functions(self):      # Parliamentary functions and political parties
		return self.functions

	def set_functions(self, fctn):
		self.functions = fctn

	
	def get_ID(self):
		return self.ID

	def set_ID(self, idx):
		self.ID = idx







	#########################################################
	####      Defining the Getters and the Setters  #########
	####				from the db file            #########
	#########################################################
	#########################################################

	

	def get_index_db(self):

		try:
			ID = self.ID
			dataset = self.dataset
			index = dataset.set_index('index').index.get_loc(ID)
		except:
			index = None

		if index == None:
			self.intruder = True
		else:
			self.intruder = False
		return index

	def get_fullName_db():
		try:
			index = get_index()
			dataset = get_dataset()
			fullmetal = dataset[index, 'fullName'] 
		except:
			fullmetal = None
		return fullmetal

	def get_firstName_db():
		full = get_fullName_db()
		fn, ln = find_space_tab(full)
		return fn

	def get_lastName_db():
		full = get_fullName_db()
		fn, ln = find_space_tab(full)
		return ln

	def get_functions_db():
		try:

			dataset = get_dataset()

			index = get_index()

			fun1 = dataset[index, 'GP'] + ' and'
			fun2 = dataset[index, 'NGP']
		except:
			fun1 = None 
			fun2 = None

		return fun1 +  fun2  

	def get_country_db():
		try:
			dataset = get_dataset()
			index = get_index()
			country = dataset[index, 'country'] 
		except:
			country = None
		return country

	def find_space_tab(url): 
	    text = url
	    iterator = 0
	    ls = []
	    for i in range(len(text)):
	        if text[i] == ' ':
	        	ls.append(i)
	    for i in range(len(ls)):
	    	if not(text[ls[i]-1].isupper()):
	    		pass

	    	else:
	    		break

	    return text[:ls[i]-1], text[ls[i]-1:]

#######################################################
########## Some other fancy functions #################
#######################################################


	# def is_intruder(self):
	# 	try:
	# 		ID = self.ID
	# 		dataset = self.dataset
	# 		index = dataset.set_index('index').index.get_loc(ID)
	# 	except:
	# 		index = None
		




