from rest_framework import routers
from .api import AuthorViewSet, CategoryViewSet, TagViewSet, GenreViewSet, LocationViewSet, PlayerViewSet, PostViewSet, LinkTypeViewSet, LinkViewSet


router = routers.DefaultRouter()


router.register('api/authors', AuthorViewSet, 'authors')
router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/genres', GenreViewSet, 'genres')
router.register('api/locations', LocationViewSet, 'locations')
router.register('api/players', PlayerViewSet, 'players')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/linktypes', LinkTypeViewSet, 'linktypes')
router.register('api/links', LinkViewSet, 'links')


urlpatterns = router.urls
