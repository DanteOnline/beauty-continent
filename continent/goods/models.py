from django.db import models
from categories.models import Subcategory
from django_comments.models import Comment
#для удаления картинок
from generic.models import ImageManager
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            db_index=True,
                            verbose_name='Название')
    category = models.ForeignKey(Subcategory, verbose_name='Категория')
    description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Полное описание')
    price = models.FloatField(db_index=True, verbose_name='Цена, руб.')

    def get_price(self):
        return str(round(self.price)) + ' руб.'

    price_acc = models.FloatField(null=True, blank=True,
                                  verbose_name='Цена с учетом скидки, руб.')
    #на товар есть скидка
    def is_with_discount(self):
        if self.price_acc:
            return True
        else:
            return False
    #Есть в наличии
    in_stock = models.BooleanField(default=True, db_index=True,
                                   verbose_name='Есть в наличии')
    #Новый товар
    is_new = models.BooleanField(default=False, db_index=True,
                                   verbose_name='Новый')
    #Популярный товар
    def is_popular(self):
        return False

    #Отзывы
    def comments(self):
        comments = Comment.objects.filter(object_pk=self.pk)
        return comments

    #Количество отзывов
    def comments_count(self):
        comments = self.comments()
        return len(comments)

    #рейтинг
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг', default=4)

    image = models.ImageField(upload_to='goods/list',
                              verbose_name='Основное изображение')

    def __init__(self,*args,**kwargs):
        self.image_manager = ImageManager(self,Good)
        super(Good, self).__init__(*args,**kwargs)

    def save(self, *args, **kwargs):
        self.image_manager.save()
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image_manager.delete()
        super(Good, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['category', 'is_new', 'price', 'name']

@receiver(pre_delete, sender=Good)
def _mymodel_delete(sender, instance, **kwargs):
    instance.image_manager.delete()

from django_comments.moderation import CommentModerator, moderator

class GoodModerator(CommentModerator):
    email_notification = True
moderator.register(Good, GoodModerator)

class GoodImage(models.Model):
    good = models.ForeignKey(Good)
    image = models.ImageField(upload_to='goods/detail', verbose_name='Дополнительное изображение')

    def __init__(self,*args,**kwargs):
        self.image_manager = ImageManager(self,GoodImage)
        super(GoodImage, self).__init__(*args,**kwargs)

    def save(self, *args, **kwargs):
        self.image_manager.save()
        super(GoodImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image_manager.delete()
        super(GoodImage, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    class Meta:
        verbose_name = 'изображение к товару'
        verbose_name_plural = 'изображения к товару'

@receiver(pre_delete, sender=GoodImage)
def _mymodel_delete(sender, instance, **kwargs):
    instance.image_manager.delete()