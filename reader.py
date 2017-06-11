import os
from album import Album


def get_albums_in_folder(path_to_top_folder):
    """Return array of album objects"""
    albums = []
    for root, dirs, files in os.walk(path_to_top_folder):
        for name in dirs:
            new_album = Album()
            new_album.title = name
            new_album.path = os.path.join(root, name)

            for root, dirs, files in os.walk(new_album.path):
                new_album.num_tracks += len(files)

            albums.append(new_album)

    return albums


get_albums_in_folder('YG/')
