import pygame
from MusicQueue import MusicQueue
import random
import time
from LEDController import LEDController

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
		self.led_toggler = LEDController()
		self.volume_context = 0.5
		
	def initialize(self):
		pygame.mixer.init()
		print("Initializing MuseBox...")
		self.mixer_context.stop()
		self.is_playing = False
		self.is_loaded = False
		#self.queue.reset_songs()

	def play_music(self):
		if (not self.is_loaded):
			# Load music and play
			print("Loading music...")
			self.songs_to_play = self.queue.get_songs(limit=50) 		
			self.max_song_queue_pos = len(self.songs_to_play)
			selected_song = self.songs_to_play[self.queue_pos]
			self.mixer_context.load(selected_song)
			self.mixer_context.set_volume(self.volume_context)
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
		self.led_toggler.playing()
		return
    
	def pause_music(self):
		if (self.is_playing):
			print("Pausing music...")
			self.mixer_context.pause()
			self.is_playing = False
			self.led_toggler.paused()
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
		self.led_toggler.playing()
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
		
	def rewind_current_song(self):
		'''
			Restarts the currently playing song.
		'''
		if (self.is_playing):
			print("Restarting song")
			self.mixer_context.rewind()
		else:
			print("Nothing to rewind")
		return
		
	def previous_song(self):
		'''
			Play the song that played before the current song, if the queue
			supports this action. 
			
			Caveats:
		'''
		if (self.is_loaded):
			print("Playing previous song...")
			if (self.queue_pos >= 1):
				self.is_loaded = False
				self.is_playing = False
				self.queue_pos -= 1
				self.show_song()
				self.mixer_context.load(self.songs_to_play[self.queue_pos])
				self.is_loaded = True
				self.mixer_context.play()
				self.is_playing = True
				self.led_toggler.playing()
			else:
				print("No previous song in queue.")
		else:
			print("no songs loaded.")
		return
		
		
	def show_song(self):
		print("Playing song: {0}".format(self.songs_to_play[self.queue_pos]))
		
		
	def volume_up(self):
		current_volume = self.mixer_context.get_volume()
		new_volume = 0
		if (current_volume + 0.1 < 1.0):
			new_volume = current_volume + 0.1
		else:
			new_volume = 1.0
		print("new volume after up is: {0}".format(new_volume))
		self.volume_context = new_volume
		self.mixer_context.set_volume(self.volume_context)
    
	def volume_down(self):
		current_volume = self.mixer_context.get_volume()
		new_volume = 0
		if (current_volume - 0.1 > 0.0):
			new_volume = current_volume - 0.1
		else:
			new_volume = 0
		print("new volume after down is: {0}".format(new_volume))
		self.volume_context = new_volume
		self.mixer_context.set_volume(self.volume_context)

	def reset(self):
		'''
			Resets everything related to this object. Turns off all 
			of the Raspberry Pi lights. Also uninitializes 
			the pygame mixer. Before using MuseBox again, initialize 
			must be called on the MusicController object.
			
			Does NOT destory the actual MusicController object. 
			This is because we need to preserve the volume setting.
		'''
		self.mixer_context.stop()
		self.is_loaded = False
		self.is_playing = True
		self.queue_pos = 0
		self.led_toggler.turn_off_all_lights()
		pygame.mixer.quit()
		return
