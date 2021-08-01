from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class GamePost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    ICON_CHOICES = (
        ('icon-android', 'icon-android'),
        ('icon-windows', 'icon-windows'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="img/")
    icon = models.CharField(max_length=20,
                              choices=ICON_CHOICES,
                              default='icon-android')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:games_post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

class AboutUs(models.Model):
    POSITIONS = (
        ('Programmer', 'Programmer'),
        ('Graphics Designer', 'Graphics Designer'),
    )
    SOCIAL_ICONS = (
        ('icon-linkedin-squared', 'icon-linkedin-squared'),
        ('icon-github-circled-alt2', 'icon-github-circled-alt2'),
        ('https://img.icons8.com/ios/50/000000/sketchfab.png', 'https://img.icons8.com/ios/50/000000/sketchfab.png'),
        ('https://img.icons8.com/windows/50/000000/artstation.png', 'https://img.icons8.com/windows/50/000000/artstation.png'),
    )
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50,
                                choices=POSITIONS,
                                default='Programmer')
    social_icon_first = models.CharField(max_length=255,
                                         choices = SOCIAL_ICONS,
                                         default = 'icon-linkedin-squared')
    social_icon_first_link = models.CharField(max_length=255,
                                              null = True,
                                              blank= True)
    social_icon_second = models.CharField(null=True,
                                          blank=True,
                                         max_length=255,
                                         choices = SOCIAL_ICONS)
    social_icon_second_link = models.CharField(max_length=255,
                                              null=True,
                                               blank=True)
    social_icon_third = models.CharField(null=True,
                                         blank=True,
                                         max_length = 255,
                                         choices= SOCIAL_ICONS)
    social_icon_third_link = models.CharField(max_length=255,
                                               null=True,
                                              blank=True)
    social_icon_fourth = models.CharField(null=True,
                                         blank=True,
                                         max_length=255,
                                         choices=SOCIAL_ICONS)
    social_icon_fourth_link = models.CharField(max_length=255,
                                              null=True,
                                              blank=True)
    person_img = models.ImageField(null=True, blank=True, upload_to="img/")
    person_info = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.surname



class ContactUs(models.Model):
    SOCIAL_MEDIA = (
        ('icon-instagram', 'icon-instagram'),
        ('icon-facebook-squared', 'icon-facebook-squared'),
    )
    address_email = models.CharField(max_length=30)
    social_media_first = models.CharField(max_length=40,
                                          choices = SOCIAL_MEDIA,
                                          default = 'icon-instagram')
    social_media_first_link = models.CharField(max_length=255,
                                               null=True,
                                               blank=True)
    social_media_second = models.CharField(max_length=40,
                                          choices=SOCIAL_MEDIA,
                                          default='icon-facebook-squared')
    social_media_second_link = models.CharField(max_length=255,
                                                null=True,
                                                blank=True)