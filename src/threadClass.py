import threading
import time

"""

This thread class is a modified version which allows to collect output from functions

"""


class Thread(threading.Thread):
	def __init__(self, function, args = (), timez = 0):
		super(Thread, self).__init__() # Calls the init function of the mother class threading.Thread
		self.function = function
		self.args = args
		self.timez = timez

	def run(self):
		time.sleep(self.timez)
		self.result = self.function(*self.args)

	def get_result(self):
		threading.Thread.join(self)

		try:
			return self.result
		except Exception:
			return None

	def pause (self):
		self.__flag.clear() #set to false, let the thread block

	def resume (self):
		self.__flag.set() #Set to true to stop the thread from blocking


	def stop (self):
		self.__flag.set() #resume the thread from the suspended state, How has it been suspended
		self.__running.clear() #set to false




