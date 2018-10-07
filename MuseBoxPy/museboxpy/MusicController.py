import pygame
from MusicQueue import MusicQueue

class MusicController():
    def __init__(self):
        self.is_loaded = False
        self.is_playing = False
        self.queue = MusicQueue()
        self.mixer_context = pygame.mixer.music
        pygame.mixer.init()
        
    def reset(self):
        print("Reseting Music Controller")
        self.mixer_context.stop()
        self.is_playing = False
        self.has_music_loaded = False
        self.queue.reset_songs()

    def play_music(self):
        if (not self.is_loaded):
            # Load music and play
            print("Loading music...")
            songs_to_play = self.queue.get_songs(limit=50) 
            for song in songs_to_play:
                self.mixer_context.queue(song)
            print("Playing music...")
            self.mixer_context.play()
            # self.mixer_context.set_endevent(pygame.USEREVENT + 1)
            self.is_loaded = True
            self.is_playing = True
        if (self.is_loaded):
            # Music is already loaded, assume in progress and unpause
            print("Resuming music...")
            self.mixer_context.unpause()
            self.is_playing = True
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
            
    def next_song(self):
        '''
            Stupid way of playing a new song.
            Requeues all of the songs and starts playing them again.
            No guarentee that the song will not have already been played
            with this method.
        '''
        print("Playing next song...")
        self.mixer_context.stop()
        self.is_loaded = False
        self.is_playing = False
        self.play_music()
        return
    
