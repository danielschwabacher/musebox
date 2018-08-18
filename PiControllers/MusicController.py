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
		'''
			Cases:
			1.) music loaded and playing
			2.) music loaded and not playing
			3.) music not loaded and playing -- impossible
			4.) music not loaded and not playing
		'''
		if (self.has_music_loaded):
			if (self.is_playing):
				# Pause music
				print("Pausing music...")
				self.mixer_context.pause()
				self.is_playing = False
			else:
				print("Resuming music...")
				self.mixer_context.unpause()
				self.is_playing = True
		else:
			print("Loading music...")
			song_to_play = self.queue.get_random_song()
			self.mixer_context.load(song_to_play)
			self.has_music_loaded = True
			print("Playing music...")
			self.mixer_context.play()
			self.is_playing = True
			
	
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
