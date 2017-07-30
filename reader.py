import os
import sys
from album import Album

def get_albums_for_artist(path_to_artist):
    """Return array of album objects"""
    albums = []
    for root, dirs, files in os.walk(path_to_artist):
        for name in dirs:
            new_album = Album()
            new_album.title = name
            new_album.path = os.path.join(root, name)

            for root, dirs, files in os.walk(new_album.path):
                new_album.num_tracks += len(files)

            albums.append(new_album)

    return albums


if __name__ == "__main__":
    albums = get_albums_for_artist(sys.argv[1])

    for album in albums:
        print album

