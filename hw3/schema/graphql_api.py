from graphene import ObjectType, Schema, String, Int, List, Field
from starlette.graphql import GraphQLApp

from hw3.model.album import Album
from hw3.model.artist import Artist
from hw3.model.track import Track
from hw3.service import track_service, artist_service, album_service


class ArtistQuery(ObjectType):
    id = Int()
    name = String()


class TrackQuery(ObjectType):
    id = Int()
    title = String()
    language = String()
    artists = List(ArtistQuery)

    def resolve_artists(self, info):
        artists = artist_service.get_artists_by_track_id(self.id)
        return [convert_artist(artist) for artist in artists]


class AlbumQuery(ObjectType):
    id = Int()
    tracks = List(TrackQuery)
    artists = List(ArtistQuery)
    title = String()
    genre = String()
    type = String()

    def resolve_tracks(self, info):
        tracks = track_service.get_tracks_by_album_id(self.id)
        return [convert_track(track) for track in tracks]

    def resolve_artists(self, info):
        artists = artist_service.get_artists_by_album_id(self.id)
        return [convert_artist(artist) for artist in artists]


class Query(ObjectType):
    album = Field(AlbumQuery, id=Int(required=True))
    track = Field(TrackQuery, id=Int(required=True))
    artist = Field(ArtistQuery, id=Int(required=True))

    def resolve_album(self, info, id):
        return convert_album(album_service.get_by_id(id))

    def resolve_track(self, info, id):
        return convert_track(track_service.get_by_id(id))

    def resolve_artist(self, info, id):
        return convert_artist(artist_service.get_by_id(id))


def convert_album(album: Album):
    return AlbumQuery(id=album.id,title=album.title, genre=album.genre, type=album.type)


def convert_artist(artist: Artist):
    return ArtistQuery(id=artist.id, name=artist.name)


def convert_track(track: Track):
    return TrackQuery(id=track.id, title=track.title, language=str(track.language))


app = GraphQLApp(schema=Schema(query=Query))
