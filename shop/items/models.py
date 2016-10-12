from django.db import models
from django_comments.models import Comment
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50,unique=True,db_index=True,verbose_name='Название')
    description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(blank=True,null=True,name='Полное описание')
    price = models.FloatField(db_index=True,default=0,verbose_name='Цена')

    def get_price(self):
        return str(round(self.price)) + ' руб.'

    price_acc = models.FloatField(null=True,blank=True,verbose_name='Цена с учетом скидки')
    #есть ли скидка
    def is_discount(self):
        if self.price_acc:
            return True
        else:
            return False
    #процент скидки
    def discount_percent(self):
        if self.is_discount():
            return (self.price_acc/self.price)*100
        else:
            return 0

    def get_percent(self):
        return str(round(self.discount_percent())) + ' %'

    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='Есть в наличии')
    is_new = models.BooleanField(default=False, db_index=True, verbose_name='Новый товар')

    is_popular = models.BooleanField(default=False, db_index=True, verbose_name='Популярный')

    # Отзывы
    def comments(self):
        comments = Comment.objects.filter(object_pk=self.pk)
        return comments

    # Количество отзывов
    def comments_count(self):
        comments = self.comments()
        return len(comments)

    # рейтинг
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг', default=4, validators=[MaxValueValidator(5),MinValueValidator(0)])

    #изображение
    image = models.ImageField(upload_to='items/list', verbose_name='Основное изображение')

    #родитель
    parent = models.ForeignKey('self', blank=True, null=True)

    TOP = 'TO'
    NODE = 'NO'
    LEAF = 'LE'
    ITEM_TYPES = (
        (TOP, 'Вершина'),
        (NODE,'Узел'),
        (LEAF,'Лист')
    )
    #Тип объекта
    item_type = models.CharField(db_index=True, max_length=2, verbose_name='Тип', choices=ITEM_TYPES, default=TOP)

    def __str__(self):
        return self.name

    def is_leaf(self):
        return self.item_type == self.LEAF

    def get_children(self):
        if self.is_leaf():
            return None
        else:
            children = Item.objects.filter(parent = self)
            return children

    @staticmethod
    def get_tops():
        tops = Item.objects.filter(item_type = Item.TOP)
        return tops

    def get_url(self):
        return reverse('item', kwargs={'pk': self.pk})

#from django.contrib.comments.moderation import CommentModerator, moderator
from django_comments.moderation import CommentModerator, moderator

class ItemModerator(CommentModerator):
    email_notification = True
moderator.register(Item, ItemModerator)