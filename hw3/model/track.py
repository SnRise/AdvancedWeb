from enum import Enum
from typing import List

from pydantic import BaseModel


class Language(Enum):
    RU = 1
    EN = 2
    KZ = 3


class Track(BaseModel):
    id: int
    album_id: int
    artist_ids: List[int]
    title: str
    language: Language
