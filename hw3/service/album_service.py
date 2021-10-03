from hw3.db.db import albums


def get_by_id(id: int):
    return albums[id]

