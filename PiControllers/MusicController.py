import pygame
from MusicQueue import MusicQueue
import random
import time

NEXT_SONG = pygame.USEREVENT + 1
class MusicController():
	def __init__(self):
		self.is_loaded = False
		self.is_playing = False
		self.queue = MusicQueue()
		self.mixer_context = pygame.mixer.music
		self.songs_to_play = []
		self.queue_pos = 0
		self.max_song_queue_pos = 0
		
	def reset(self):
		pygame.mixer.init()
		print("Reseting MuseBox...")
		self.mixer_context.stop()
		self.is_playing = False
		self.is_loaded = False
		#self.queue.reset_songs()

	def play_music(self):
		if (not self.is_loaded):
			# Load music and play
			print("Loading music...")
			self.songs_to_play = self.queue.get_songs(limit=5) 		
			self.max_song_queue_pos = len(self.songs_to_play)
			selected_song = self.songs_to_play[self.queue_pos]
			self.mixer_context.load(selected_song)
			print("Playing song: {0}".format(selected_song))
			self.mixer_context.play()
			self.mixer_context.set_endevent(NEXT_SONG)
			self.is_loaded = True
			self.is_playing = True			
		elif (self.is_loaded):
			# Music is already loaded, assume in progress and unpause
			print("Resuming music...")
			self.mixer_context.unpause()
			self.is_playing = True
		# self.queue_pos += 1
		return
    
	def pause_music(self):
		if (self.is_playing):
			print("Pausing music...")
			self.mixer_context.pause()
			self.is_playing = False
		return

	def toggle(self):
		if (self.is_playing):
			self.pause_music()
		else:
			self.play_music()
	
	def resume_from_queue(self):
		self.queue_pos += 1
		self.show_song()
		self.mixer_context.load(self.songs_to_play[self.queue_pos])
		self.is_loaded = True
		self.mixer_context.play()
		self.is_playing = True
		return
	
	def next_song(self):
		'''
			Try to play from queue if there are songs left.
			Otherwise, requeue songs and play.
		'''
		print("Playing next song...")
		if (self.is_loaded):
			if (self.queue_pos + 1 < self.max_song_queue_pos):
				self.mixer_context.stop()
				self.is_loaded = False
				self.is_playing = False
				self.resume_from_queue()
			else:
				self.queue_pos = 0
				self.mixer_context.stop()
				self.is_loaded = False
				self.is_playing = False
				self.play_music()
		else:
			self.play_music()
		return
		
		
	def show_song(self):
		print("Playing song: {0}".format(self.songs_to_play[self.queue_pos]))
    
