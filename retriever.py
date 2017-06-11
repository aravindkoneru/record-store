import musicbrainzngs

musicbrainzngs.set_useragent(
    "bulk_record_organizer",
    "0.1",
    "https://github.com/aravindkoneru"
)


def search_for_release(album_title):
    """
    Returns a release id given an album title
    """
    # @TODO: Make selective/interactive
    release_candidates = musicbrainzngs.search_releases(
        query=album_title, strict=True)
    release_id = release_candidates['release-list'][0]['id']
    return release_id


def get_release_info(release_id):
    """
    Returns release info given an id
    """
    release_info = musicbrainzngs.get_release_by_id(
        id=release_id, includes=['tags', 'recordings'])
    return release_info

release_id = search_for_release("still brazy")
print get_release_info(release_id)
