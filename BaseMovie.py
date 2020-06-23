
class BaseMovie:

    def __init__(self, title, initial_release, content_type):
        self.title = title
        self.initial_release = initial_release
        self.content_type = content_type

        self._number_plays = 0
            
    def __str__(self):
        return f'{self.title} ({self.initial_release})'
    def __repr__(self):
        return f"BaseMovie(title={self.title} , initial_release={self.initial_release}, content_type={self.content_type})"
    def __eq__(self, other):
        return all (
            (self.name == other.name,
            self.lastname == other.lastname,
            self.mobile == other.mobile,
            self.mail == other.mail
            )
        )
    def play(self):
       self._number_plays += 1

    @property
    def label_length(self):
        return ((str(len(self.name)) +" "+str(len(self.lastname))))