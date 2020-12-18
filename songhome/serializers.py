from rest_framework import serializers
from .models import Song, Comment, Writer, Tag, Genre


class CommentSerializer(serializers.ModelSerializer):
    # song = serializers.ReadOnlyField(source='song.id', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'song', 'status', 'text', 'created',)


class WriterSerializer(serializers.ModelSerializer):
    # song_name = serializers.ReadOnlyField(source='song.name', read_only=True)

    class Meta:
        model = Writer
        fields = ('id', 'name', 'pub_percent', 'song')


class SongLimitedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'name', 'status')


class TagSerializer(serializers.ModelSerializer):
    song = SongLimitedSerializer(many=False, read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'song')


class GenreSerializer(serializers.ModelSerializer):
    # song = SongLimitedSerializer(many=False, read_only=True)

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
    
    def create(self, data):
        
        song = Song.objects.create(**data)
        print(data)
        print(song)

        return song
