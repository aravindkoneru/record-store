import musicbrainzngs

musicbrainzngs.set_useragent(
    "bulk_record_organizer",
    "0.1",
    "https://github.com/aravindkoneru"
)


def __search_for_release(album_title):
    """Return a release id given an album title."""
    # @TODO: Make selective/interactive
    release_candidates = musicbrainzngs.search_releases(
        query=album_title, strict=True)
    release_id = release_candidates['release-list'][0]['id']

    return release_id


def get_release_info(album_title):
    """Return release info given an id."""
    release_id = __search_for_release(album_title)
    release_info = musicbrainzngs.get_release_by_id(
        id=release_id, includes=['tags', 'recordings'])

    return release_info


def info_parser(album_info):

    to_print = album_info['release']['medium-list'][0]['track-list']

    for x in range(0, len(to_print)):
        print to_print[x], "\n"

    # for key in to_print:
    #     print "key: {}".format(key)
    #     print to_print[key]
