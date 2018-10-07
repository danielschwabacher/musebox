import os
import random
class MusicQueue():
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.music_dirs = [self.home_dir + "/CranberryMusic/mp3s/"]
        self.played_songs = []
        self.queued_songs = []
        self.number_songs_in_dir = len(os.listdir(self.music_dir))

    def clear_queue(self):
        self.played_songs = []

    def get_queued_songs(self):
        return queued_songs
    
    def get_all_songs(self, limit=50):
        '''
            Returns a list of all the music files (mp3s) 
            under inside the music dir directory.
            Limit specifies the maximum number of files to return
        '''
        lim = limit
        song_files = []
        for directory in self.music_dirs:
            for song in os.listdir(directory):
                if (lim <= limit):
                    song_files.append(song)
                    lim += 1
                else:
                    break
        return random.shuffle(song_files)
        
    def get_next_song(self):
        return 

