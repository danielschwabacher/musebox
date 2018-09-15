import os
import random
class MusicQueue():
	
	def __init__(self):
		self.home_dir = os.path.expanduser("~")
		#self.music_dirs = [self.home_dir + "/CranberryMusic/mp3s/"]
		self.music_dirs = [self.home_dir + "/test_music/"]
		self.played_songs = []
		self.queued_songs = []
		self.number_songs_in_dir = self.calculate_number_songs()
		self.already_played_songs = []

	def calculate_number_songs(self):
		total_songs = 0
		for directory in self.music_dirs:
			total_songs += len(os.listdir(directory))
		return total_songs
		
	def get_songs(self, limit=50):
		'''
		Returns a list of all the music files (mp3s) 
		under inside the music dir directory.
		Limit specifies the maximum number of files to return
		'''
		lim = 0
		song_files = []
		song_files_no_path_prefix = []
		for directory in self.music_dirs:
			for song in random.sample(os.listdir(directory), len(os.listdir(directory))):
				if (lim < limit):
					if (song not in self.already_played_songs):
						song_files.append(directory + song)
						song_files_no_path_prefix.append(song)
						lim += 1
					else:
						continue
				else:
					break
		print("Songs returned: {0}".format(song_files_no_path_prefix))
		return song_files
		

	def finish_song(self, song):
		self.already_played_songs.append(song)
		
