from hw3.model.album import Album, AlbumType
from hw3.model.artist import Artist
from hw3.model.track import Track, Language

artists = {
    1: Artist(id=1, name="Slava Marlow"),
    2: Artist(id=2, name="Алишер Моргенштерн"),
    3: Artist(id=3, name="Данила Поперечный"),
    4: Artist(id=4, name="Гарик Харламов"),
    5: Artist(id=5, name="Кайрат Нуртас")
}

tracks = {
    1: Track(
        id=1,
        album_id=1,
        artist_ids=[1, 2],
        title="Cadillac",
        language=Language.RU
    ),
    2: Track(
        id=2,
        album_id=1,
        artist_ids=[1, 2],
        title="Ice",
        language=Language.RU
    ),
    3: Track(
        id=3,
        album_id=1,
        artist_ids=[2],
        title="Leck",
        language=Language.EN
    ),
    4: Track(
        id=4,
        album_id=2,
        artist_ids=[2, 3],
        title='СУД ЗА ПРОПАГАНДУ, ЕГО ЗАВИСИМОСТИ, МузТВ, ПЕРФОРМАНСЫ и STALKER 2',
        language=Language.RU
    ),
    5: Track(
        id=5,
        album_id=2,
        artist_ids=[3, 4],
        title='Развод, "Гусар", 18 лет Comedy, новый "Ну, погоди!" и о чувстве смешного',
        language=Language.RU
    ),
    6: Track(
        id=6,
        album_id=3,
        artist_ids=[5],
        title="Мен Оралам",
        language=Language.KZ
    ),
}

albums = {
    1: Album(
        id=1,
        track_ids=[1, 2, 3],
        artist_ids=[1, 2],
        title="Million Dollar Business",
        genre="Русский рэп",
        type=AlbumType.MUSIC
    ),
    2: Album(
        id=2,
        track_ids=[4, 5],
        artist_ids=[2, 3, 4],
        title="Без души",
        genre="Подкасты",
        type=AlbumType.PODCAST
    ),
    3: Album(
        id=3,
        track_ids=[6],
        artist_ids=[5],
        title="Мен Оралам",
        genre="Каз поп",
        type=AlbumType.SINGLE
    ),
}
