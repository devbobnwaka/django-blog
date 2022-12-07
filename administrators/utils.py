import random
from django.utils.text import slugify


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    rand_int = random.randint(300_000, 500,000)
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