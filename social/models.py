import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_body

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return "{} . {} ".format(self.id, self.author)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



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