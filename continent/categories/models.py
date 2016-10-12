from django.db import models
from django.core.urlresolvers import reverse
#для удаления картинок
from generic.models import ImageManager
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30, db_index = True, unique = True, verbose_name = 'Название')
    order = models.PositiveSmallIntegerField(default = 0, db_index = True, verbose_name = 'Порядковый номер')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Subcategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Название')
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='Порядковый номер')
    parent = models.ForeignKey(Category)
    image = models.ImageField(upload_to='subcategories/list', verbose_name='Основное изображение', null=True, blank=True)

    def is_get_image(self):
        if self.image:
            return True
        else:
            return False

    def __init__(self,*args,**kwargs):
        self.image_manager = ImageManager(self,Subcategory)
        super(Subcategory, self).__init__(*args,**kwargs)

    def save(self, *args, **kwargs):
        self.image_manager.save()
        super(Subcategory, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image_manager.delete()
        super(Subcategory, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['parent','order', 'name']
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

@receiver(pre_delete, sender=Subcategory)
def _mymodel_delete(sender, instance, **kwargs):
    instance.image_manager.delete()