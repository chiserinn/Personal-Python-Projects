class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics    

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
            

kathleen = ["You're simpatico", "And of all the lift-homes and all the mixed feelings","You're cuts above", "And you don't own worries or a chest full of heartache", "Yes, I know", "That I'll never work out exactly how you­'re thinking"]
song = Song(kathleen)


song.sing_me_a_song()