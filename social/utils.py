import random
from django.utils.text import slugify





def slugify_instance_body(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.body)
    Klass = instance.__class__
    bd = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if bd.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_body(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
