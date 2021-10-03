from enum import Enum
from typing import List

from pydantic import BaseModel


class AlbumType(Enum):
    MUSIC = 1
    SINGLE = 2
    PODCAST = 3
    AUDIOBOOK = 4


class Album(BaseModel):
    id: int
    track_ids: List[int]
    artist_ids: List[int]
    title: str
    genre: str
    type: AlbumType
