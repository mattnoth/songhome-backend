from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, CommentViewSet, WriterViewSet, TagViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'writers', WriterViewSet, basename='writer')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'genres', GenreViewSet, basename='genre')
urlpatterns = router.urls
