from rest_framework import viewsets, permissions
from .models import Author, Category, Tag, Genre, Location, Player, Post, LinkType, Link
from .serializers import AuthorSerializer, CategorySerializer, TagSerializer, GenreSerializer, LocationSerializer, PlayerSerializer, PostSerializer, LinkTypeSerializer, LinkSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = TagSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = GenreSerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = PlayerSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer


class LinkTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LinkType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = LinkTypeSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = LinkSerializer
