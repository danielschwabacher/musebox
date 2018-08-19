import os
import random
class MusicQueue():
	def __init__(self):
		self.home_dir = os.path.expanduser("~")
		self.music_dir = self.home_dir + "/CranberryMusic/mp3s/"
		self.played_songs = []
		self.number_songs_in_dir = len(os.listdir(self.music_dir))
	
	def reset_songs(self):
		self.played_songs = []
			
	def get_random_song(self):
		if (self.number_songs_in_dir == len(self.played_songs)):
			self.reset_songs()
		random_file = random.choice(os.listdir(self.music_dir))
		if (random_file not in self.played_songs):
			print("Playing song: " + str(random_file))
			self.played_songs.append(random_file)
			path = os.path.join(self.music_dir, random_file)
			return path
		else:
			return self.get_random_song()
			
		
