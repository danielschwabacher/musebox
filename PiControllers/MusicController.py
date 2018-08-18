import pygame
from MusicQueue import MusicQueue

class MusicController():
	def __init__(self):
		self.is_playing = False
		self.queue = MusicQueue()
		self.mixer_context = pygame.mixer.music
		pygame.mixer.init()
		
	def play(self):
		if (self.is_playing):
			print("Stopping music...")
			self.is_playing = not (self.is_playing)
			self.mixer_context.stop()
		else:
			print("Playing music...")
			self.is_playing = not (self.is_playing)
			song_to_play = self.queue.get_random_song()
			self.mixer_context.load(song_to_play)
			self.mixer_context.play()
