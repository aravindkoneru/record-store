import reader
import retriever
import writer

albums = reader.get_albums_in_folder('YG/')

for album in albums:
    album_info = retriever.get_release_info(album.title)
    writer.read_info(album)