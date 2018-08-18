import os
import random
class MusicQueue():
	def __init__(self):
		self.home_dir = os.path.expanduser("~")
		self.music_dir = self.home_dir + "/CranberryMusic/mp3s/"
	def get_random_song(self):
		random_file = random.choice(os.listdir(self.music_dir))
		path = os.path.join(self.music_dir, random_file)
		return path
		
		
