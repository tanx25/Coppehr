from django.db import models


class PostStatus(models.TextChoices):  # Event
    DRAFT = 'DR', 'Draft'
    IN_REVIEW = 'IN', 'In Review'
    REVIEWED = 'RE', 'Reviewed'
    PUBLISHED = 'PU', 'Published'


class PostCategory(models.TextChoices):  # Category
    HEALTH = 'HE', 'Health'
    FRIENDSHIP = 'FR', 'Friendship'
    SUPPORT = 'SU', 'Support'


class Venue(models.Model):
    class Type(models.TextChoices):
        WEBSITE = 'WE', 'Website'
        ZOOM = 'ZO', 'Video Conference'
        VIDEO = 'VI', 'Video'
        FILE = 'FI', 'File'

    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    type = models.CharField(max_length=2,
                            choices=Type.choices,
                            default=Type.WEBSITE)

    def __str__(self) -> str:
        return f'Venue({self.name})'


class HealthTip(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    release_date = models.DateField(
        help_text='Monday of the week when health tip is released')
    expiration_date = models.DateField()
    status = models.CharField(max_length=2,
                              choices=PostStatus.choices,
                              default=PostStatus.DRAFT)
    published_on = models.DateTimeField(blank=True,
                                        null=True,
                                        help_text='Date and time of publication')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'HealthTip({self.title})'


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=2,
                                choices=PostCategory.choices,
                                default=PostCategory.HEALTH)
    text = models.TextField()
    release_date = models.DateField(
        help_text='Monday of the week when announcement is released')
    expiration_date = models.DateField()
    status = models.CharField(max_length=2,
                              choices=PostStatus.choices,
                              default=PostStatus.DRAFT)
    published_on = models.DateTimeField(blank=True,
                                        null=True,
                                        help_text='Date and time of publication')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Announcement({self.title})'


class Event(models.Model):
    title = models.CharField(max_length=200)
    series_title = models.CharField(max_length=200,
                                    blank=True)
    category = models.CharField(max_length=2,
                                choices=PostCategory.choices,
                                default=PostCategory.HEALTH)
    slug = models.SlugField(max_length=200,
                            unique_for_date='release_date',
                            help_text='Append release date: slug-YY-MM-DD')
    release_date = models.DateField(
        help_text='Monday of the week when event is released')
    description = models.TextField()
    art_uri = models.CharField(max_length=200,
                               unique_for_date='release_date')
    art_alt = models.CharField(max_length=200)
    art_caption = models.CharField(max_length=200,blank=True)
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)
    status = models.CharField(max_length=200,
                              choices=PostStatus.choices,
                              default=PostStatus.DRAFT)
    published_on = models.DateTimeField(blank=True,
                                        null=True,
                                        help_text='Date of publication')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Event({self.title}--{self.category})'


class Resource(models.Model):
    title = models.CharField(max_length=200)
    series_title = models.CharField(max_length=200,
                                    blank=True)
    category = models.CharField(max_length=2,
                                choices=PostCategory.choices,
                                default=PostCategory.HEALTH)
    slug = models.SlugField(max_length=200,
                            unique_for_date='release_date',
                            help_text='Append release date: slug-YY-MM-DD')
    release_date = models.DateField(
        help_text='Monday of the week when resource is released')
    description = models.TextField()
    art_uri = models.CharField(max_length=200,
                               unique_for_date='release_date')
    art_alt = models.CharField(max_length=200)
    art_caption = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)
    status = models.CharField(max_length=200,
                              choices=PostStatus.choices,
                              default=PostStatus.DRAFT)
    published_on = models.DateTimeField(blank=True,
                                        null=True,
                                        help_text='Date of publication')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Resource({self.title}--{self.category})'
