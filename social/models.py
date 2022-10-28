import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .utils import slugify_instance_body

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, editable=False)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    def __str__(self):
        return "{} . {} ".format(self.id, self.author)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio  = models.TextField(max_length=500, blank=True, null=True)
    birth_day = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    #need to install Pillow before use ImageField
    picture = models.ImageField(upload_to='uploads/profile_picture', default='uploads/profile_picture/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return "{} . {} ".format(self.user_id, self.name)
    # def save(self, *args, **kwargs):
    #     #self.slug = slugify(self.body)
    #     super(Post, self).save()



def post_pre_save(sender, instance, *args, **kwargs):
    #print(sender, instance)
    #if you uncomment bellow it means you slug field should be editable can add manually
    if instance.slug is None:
        # slug = slugify(instance.body)
        # instance.slug = slug
        slugify_instance_body(instance, save=False)

pre_save.connect(post_pre_save, sender=Post)

def post_post_save(sender, instance, created,*args, **kwargs):
    if created:
        # slug = slugify(instance.body)
        # instance.slug = slug
        # instance.save()
        slugify_instance_body(instance, save=True)

post_save.connect(post_post_save, sender=Post)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


