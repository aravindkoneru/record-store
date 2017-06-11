class Album(object):
    """Object to represent album."""

    def __init__(self):
        """"Init method."""
        self.__title = ""
        self.__num_tracks = 0
        self.__genre = ""
        self.__path = ""

    @property
    def title(self):
        return self.__title

    @property
    def num_tracks(self):
        return self.__num_tracks

    @property
    def genre(self):
        return self.__genre

    @property
    def path(self):
        return self.__path

    @title.setter
    def title(self, val):
        self.__title = val

    @num_tracks.setter
    def num_tracks(self, val):
        self.__num_tracks = val

    @genre.setter
    def genre(self, val):
        self.__genre = val

    @path.setter
    def path(self, val):
        self.__path = val

    def __str__(self):
        return "Title: {}\nNum Tracks: {}\nGenre: {}\nPath: {}".format(
            self.__title, self.__num_tracks, self.__genre, self.__path)
