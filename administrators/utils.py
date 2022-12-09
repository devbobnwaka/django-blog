import random
from django.utils.text import slugify


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    rand_int = random.randint(300_000, 500_000)
    if qs.exists():
        slug = f'{slug}-{rand_int}'
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def form_fields(field_name, form, placeholder):
    form.fields[field_name].widget.attrs['class'] = 'form-control'
    form.fields[field_name].widget.attrs['placeholder'] = placeholder
    form.fields[field_name].label_classes = ('form-control',)
    form.fields[field_name].widget.attrs['id'] = field_name


def form_select_fields(field_name, form, placeholder):
    form.fields[field_name].widget.attrs['class'] = 'form-select form-select-lg'
    form.fields[field_name].widget.attrs['id'] = field_name
    form.fields[field_name].widget.attrs['placeholder'] = placeholder
    form.fields[field_name].label_classes = ('form-control',)

def unique_filename(path):
    """
    Enforce unique upload file names.
    Usage:
    class MyModel(models.Model):
        file = ImageField(upload_to=unique_filename("path/to/upload/dir"))
    """
    import os, base64, datetime
    def _func(instance, filename):
        name, ext = os.path.splitext(filename)
        con_name = name + str(datetime.datetime.now())
        name = base64.urlsafe_b64encode(con_name.encode("utf-8"))
        return os.path.join(path, name.decode('utf-8') + ext)
    return _func


"""
#### THIS CAN ALSO FOR UNIQUE IMAGE UPLOAD ###
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/logos', filename)


file = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        verbose_name=_(u'Contact list'))
"""