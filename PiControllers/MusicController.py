import pygame
from MusicQueue import MusicQueue

class MusicController():
	def __init__(self):
		self.is_playing = False
		self.queue = MusicQueue()
		self.mixer_context = pygame.mixer.music
		self.has_music_loaded = False
		pygame.mixer.init()
		
	def toggle_start_stop(self):
		if (not self.has_music_loaded):
			print("Loading music...")
			song_to_play = self.queue.get_random_song()
			self.mixer_context.load(song_to_play)
		if (self.is_playing):
			print("Stopping music...")
			self.mixer_context.stop()
		else:
			print("Playing music...")
			self.mixer_context.play()
		self.is_playing = not (self.is_playing)
		self.has_music_loaded = True
	
	def play_new_song(self):
		if (not self.is_playing):
			print("Start music stream first.")
			return
		else:
			print("Playing next song...")
			self.mixer_context.stop()
			new_song = self.queue.get_random_song()
			self.mixer_context.load(new_song)
			self.mixer_context.play()
			self.has_music_loaded = True
			
	def quit():
		print("Powering off...")
		self.mixer_context.stop()
