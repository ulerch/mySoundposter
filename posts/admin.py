from django.contrib import admin
from .models import Author, Category, Tag, Genre, Location, Player, Post, LinkType, Link


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', 'email', ]
    list_display = ['name', 'slug', 'email', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', ]
    list_display = ['name', 'slug', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', ]
    list_display = ['name', 'slug', ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', ]
    list_display = ['name', 'slug', ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', ]
    list_display = ['name', 'slug', ]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]


@admin.register(LinkType)
class LinkTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]


class LinkAdmin(admin.TabularInline):
    model = Link
    search_fields = ['url', 'type', ]
    list_display = ['type', 'url', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug', ]
    list_display = ['title', 'slug', ]

    inlines = [
        LinkAdmin,
    ]
