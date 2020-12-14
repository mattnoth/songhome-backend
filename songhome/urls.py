from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, CommentViewSet, WriterViewSet, TagViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'writers', WriterViewSet, basename='writer')
router.register(r'tags', TagViewSet, basename='tag')
urlpatterns = router.urls
