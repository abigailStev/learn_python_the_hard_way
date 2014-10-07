class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
## End of class 'Song'

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there."])
# Passing a list of strings as the lyrics to 'Song'

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lyric_A = ["I've got sunshine", "on a cloudy day"]

sunshine = Song(lyric_A)
sunshine.sing_me_a_song()

# Don't do this! sunshine.sing_me_a_song(self) , because 'self' isn't defined outside of the class

"""
Why do I need self when I make __init__ or other functions for classes?

If you don't have self, then code like cheese = 'Frank' is ambiguous.
That code isn't clear about whether you mean the instance's cheese attribute,
or a local variable named cheese. With self.cheese = 'Frank' it's very clear
you mean the instance attribute self.cheese.
"""