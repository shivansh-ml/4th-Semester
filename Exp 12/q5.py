class MediaPlayer:
    def play(self):
        raise NotImplementedError("Subclasses must implement this method")

class AudioPlayer(MediaPlayer):
    def play(self):
        return "Playing audio file..."

class VideoPlayer(MediaPlayer):
    def play(self):
        return "Playing video file..."

# Creating instances
players = [AudioPlayer(), VideoPlayer()]

for player in players:
    print(player.play())
