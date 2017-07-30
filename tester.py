import sys
import reader
import retriever as mb_service
import writer


def main(args):
    arist_folder = args[0]

    albums = reader.get_albums_for_artist(arist_folder)

    for album in albums:
        album_info = mb_service.get_release_info(album.title)
        writer.read_info(album)
        writer.write_info(album, album_info["release"]["medium-list"])

if __name__ == "__main__":
    main(sys.argv[1:])




