
class BaseMovie:

    def __init__(self, title, initial_release, content_type):
        self.title = title
        self.initial_release = initial_release
        self.content_type = content_type

        self.number_plays = 0
            
    def __str__(self):
        #return f'{self.title} ({self.number_plays})'
        return f'{self.title} ({self.initial_release})'
    def __repr__(self):
        return f"BaseMovie(title={self.title} , initial_release={self.initial_release}, content_type={self.content_type})"
  
    def play(self):
       self.number_plays += 1
