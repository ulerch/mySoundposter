from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=80, null=False,
                            blank=False, unique=True)
    email = models.EmailField(
        max_length=80, null=False, blank=False, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Category(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=80, null=False,
                            blank=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Tag(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=80, null=False,
                            blank=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Genre(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=80, null=False,
                            blank=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Location(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=80, null=False,
                            blank=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Player(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True, db_index=True)
    regex = models.TextField(null=False, blank=False)
    iframe_code = models.TextField(null=False, blank=False)
    wordpress_code = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Player'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Post(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    slug = models.SlugField(max_length=80, null=False, blank=False)
    player = models.ForeignKey(
        Player, on_delete=models.PROTECT, null=False, blank=False)
    player_source = models.URLField(null=False, blank=False)
    player_source_id = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    additional_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    meta = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, null=True, blank=True, db_index=True)
    submission = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    last_updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return '%s by %s' % (self.title, self.author.name)


class LinkType(models.Model):
    name = models.CharField(max_length=40, null=False,
                            blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    class_name = models.SlugField(
        max_length=10, null=False, blank=False, unique=True)
    class_icon = models.CharField(
        max_length=40, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Link Type'
        verbose_name_plural = 'Link Types'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)


class Link(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, blank=False, db_index=True)
    type = models.ForeignKey(
        LinkType, on_delete=models.PROTECT, null=False, blank=False)
    url = models.URLField()
    text = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Link'
        ordering = ['type', 'url']

    def __str__(self):
        return '%s (%s)' % (self.url, self.type)
