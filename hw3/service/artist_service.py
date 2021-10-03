from hw3.db.db import artists, albums, tracks


def get_by_id(id: int):
    return artists[id]


def get_artists_by_album_id(album_id: int):
    return [get_by_id(i) for i in albums[album_id].artist_ids]


def get_artists_by_track_id(track_id: int):
    return [get_by_id(i) for i in tracks[track_id].artist_ids]


