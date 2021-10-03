from hw3.db.db import tracks, albums


def get_by_id(id: int):
    return tracks[id]


def get_tracks_by_album_id(album_id: int):
    return [get_by_id(i) for i in albums[album_id].track_ids]
