from SeriesMovie import SeriesMovie


class EpisodeMovie(SeriesMovie):
    def __init__(self, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number

    def __str__(self):
        # return f'{self.title} ({self.number_plays})'
        return f'{self.title} S' + "{:02d}".format(self.season_number)+"E"+"{:02d}".format(self.episode_number)

    def __repr__(self):
        return f"SeriesMovie(title={self.title} , initial_release={self.initial_release}, content_type={self.content_type}, season_number={self.season_number}, episode_number={self.episode_number})"
