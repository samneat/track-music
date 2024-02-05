class Music:
    def __init__(self):
        self.playlist = []

    def add(self, song):
        if song == '' and isinstance(song, str):
            raise Exception("You must provide a song")
        elif song in self.playlist:
            return "You have already added this sing"
        else:
            self.playlist.append(song)

    def view(self):
        if len(self.playlist) >= 1:
            return self.playlist
        else:
            return "No songs added yet"