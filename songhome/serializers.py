from rest_framework import serializers
from .models import Song, Comment, Writer, Tag, Genre


class CommentSerializer(serializers.ModelSerializer):
    song_name = serializers.ReadOnlyField(source='song.name', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'song_name')


class WriterSerializer(serializers.ModelSerializer):
    song_name = serializers.ReadOnlyField(source='song.name', read_only=True)

    class Meta:
        model = Writer
        fields = ('id', 'name', 'pub_percent', 'song_name')


class SongLimitedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'name', 'slug', 'bpm', 'status')


class TagSerializer(serializers.ModelSerializer):
    song = SongLimitedSerializer(many=False, read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'song')

class GenreSerializer(serializers.ModelSerializer):
    song = SongLimitedSerializer(many=False, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'song')


class SongSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    writers = WriterSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'name', 'slug', 'image', 'file', 'created', 'release_date', 'isrc_code', 'bpm', 'status', 'key', 'lyrics', 'comments', 'writers', 'tags', 'genres')
