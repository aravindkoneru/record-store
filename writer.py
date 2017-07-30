import os
import eyed3


def read_info(album):
    """Read info given album object."""

    for root, dirs, files in os.walk(album.path):
        for name in files:
            audiofile = eyed3.load(os.path.join(root, name))
            print audiofile.tag.title

def write_info(album, track_info):
    print track_info

    for root, dirs, files in os.walk(album.path):
        for name in files:
                audiofile = eyed3.load(os.path.join(root, name))


